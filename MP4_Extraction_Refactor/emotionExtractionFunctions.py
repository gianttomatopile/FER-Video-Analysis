import os
import json
import cv2
from deepface import DeepFace
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def createFolder(directory, name = "extracted_images"):
    """
    Creates a unique folder in a given directory

    directory = desired folder location,
    name = name of folder default = extracted images),

    returns string of directory 
    """

    defaultName = name
    run = True
    index = 0

    while run:

        #Name wont have a 0 for first folder
        if index != 0:
            name = defaultName + str(index)
        else:
            name = defaultName
        
        #Check if name in directory
        run = checkName(directory=directory,
                        name=name)
        
        #Increase naming index
        index += 1

    try:
        #Create folder
        path = os.path.join(directory, name)
        os.mkdir(path)

        #Return name of folder
        return name
    except:
        print("Failed to make folder named", name)
        return "FAILED"
    
def checkName(directory, name):
    for directories in os.listdir(directory):
        if directories == name:
            #Return True if in directory
            return True  
    #Return false if unique
    return False

def storeData(element, directory, name):
    """
    Stores the data in a JSON file

    elemet = data to be stored,
    directory = location to store data,
    name = name of file 
    """
    try:
        path = os.path.join(directory, name)
        with open(path, 'w') as f:
            json.dump(element, f, indent=1)
        print("Stored data at:", path)
    except:
        print("Failed to create store data")

def loadData(directory):
    """
    Loads JSON files

    directory = file directory
    
    returns data
    """
    try:
        with open(directory) as f:
            element = json.load(f)
        print("Loaded data from:", directory)
        return element
    except:
        print("Failed to load data")
        return None

def verify(img1_path, img2_path, model = None, model_name = None):

    #If no model is given default will be VGG-Face
    if model == None:
        #Build model
        model_name = "VGG-Face"
        model = DeepFace.build_model(model_name)

    result = DeepFace.verify(img1_path, 
                                 img2_path, 
                                 model=model, 
                                 model_name=model_name,
                                 enforce_detection=False)
    
    return result["verified"]

def groupVerify(img1_path, img2_path, validThreshold = "0.4", model = None, model_name = None):

    #If no model is given default will be VGG-Face
    if model == None:
        #Build model
        model_name = "VGG-Face"
        model = DeepFace.build_model(model_name)
        
    df = DeepFace.find(img_path=img1_path,
                            db_path=img2_path,
                            model=model,
                            model_name=model_name,
                            prog_bar=False)

    result = df["VGG-Face_cosine"].min()

    if result <= validThreshold:
        return True
    else:
        return False

def frameExtraction(imageName):
    number = ""
    #Split image name up by "_"
    for word in imageName.split("_"):
        #Check if starts with the frame identifier "FR"
        if word[0] == "F" and word[1] == "R":
            #Record each char after initial two
            for i in range(len(word) - 2):
                number = number + word[i + 2]
    
    #Return integer of frame number
    return(int(number))

def quickAnalysis(vid_source, 
                  img_directory,
                  hc = "haarcascade_frontalface_default.xml"):
    
    imageList = []
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + hc)
    
    #Open video
    cap = cv2.VideoCapture(vid_source)
    
    #Count number of frames in a video
    vidLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    #Find all faces in all frmaes
    print("Finding face frames:")
    for i in tqdm(range(vidLength), unit="Frames"):
        #capture frame
        ret, frame = cap.read()

        #Break loop if end of no frame
        if ret == False:
            break

        #Turn frame greyscale
        greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Find faces in frame
        faces = faceCascade.detectMultiScale(greyFrame,1.1,4)

        amountOfFaces = len(faces)

        #If faces found
        if amountOfFaces != 0:
            count = 0

            """
            TODO Maybe turn into two func for crop and save img?
            """

            #Crop image down to just face and eport to dir
            for(x,y,w,h) in faces:
                cropped = frame[y:y+h, x:x+w] #crop frame down to just face
                #Format:         FrameNumber,   FaceLength,              FaceNumber
                temp_fileName = "FR"+str(i) + "_FL"+ str(len(faces)) + "_FN"+ str(count) + ".jpg"
                temp_Directory = img_directory + "\\" + temp_fileName
                imageList.append(temp_fileName) #add image to list
                cv2.imwrite(temp_Directory, cropped) #save image
                count += 1

    cap.release()

    print("Frame analysis complete. " + str(len(imageList)) + " quick faces found")

    return imageList

def detailedAnalysis(imageList, img_directory):
    DFImages = []
    print("Finding faces")
    for i in tqdm(range(len(imageList)), unit="analysis"):
        try:
            det = DeepFace.detectFace(img_path= img_directory + "\\" + imageList[i])
            DFImages.append(imageList[i])
        except:
            pass

    print("Frame analysis complete. " + str(len(DFImages)) + " detailed faces found")
    return DFImages

def contiuity(DFImages, img_directory, sub_source, model = None, model_name = None):

    #If no model is given default will be VGG-Face
    if model == None:
        #Build model
        model_name = "VGG-Face"
        model = DeepFace.build_model(model_name)

    subImages = []

    print("Continuity")
    for i in tqdm(range(len(DFImages)), unit="verifies"):
        ver = verify(img_directory + "\\" + DFImages[i], sub_source, model=model, model_name=model_name)
        if ver:
            subImages.append(DFImages[i])

    print("Continuity complete. " + str(len(subImages)) + " subject faces found")

    return subImages

def emotionDetection(subImages, img_directory):
    print("Emotion detection")

    #Subject emotion dictionary
    subEmo = {0: {'angry': 0, 'disgust': 0, 'fear': 0, 'happy': 0, 'sad': 0, 'surprise': 0, 'neutral': 0}}

    #Emotion detection for each subject verified image
    for i in tqdm(range(len(subImages))):

        #Find frame number from image name
        frameNo = frameExtraction(subImages[i])

        #Pass image directory and recieve only emotion (could expand to more but that would increase processing time)
        result = DeepFace.analyze(img_directory + "\\" + subImages[i], actions = ["emotion"])

        #Add emotions to the dictionary
        subEmo[i] = result["emotion"]

        #Add frame number to dictionary
        subEmo[i]["frame"] = frameNo

    print("Emotion detection complete")
    return subEmo

def dictToList(subEmo):

    """
    Turn into list of lists and add to graph data
    """

    frameList = []
    listList = []
    angryList = []
    disgustList = []
    fearList = []
    happyList = []
    sadList = []
    surpriseList = []
    neutralList = []

    for i in subEmo:
        frameList.append(subEmo[i]["frame"])
        angryList.append(subEmo[i]["angry"])
        disgustList.append(subEmo[i]["disgust"])
        fearList.append(subEmo[i]["fear"])
        happyList.append(subEmo[i]["happy"])
        sadList.append(subEmo[i]["sad"])
        surpriseList.append(subEmo[i]["surprise"])
        neutralList.append(subEmo[i]["neutral"])
    
    listList.append(angryList)
    listList.append(disgustList)
    listList.append(fearList)
    listList.append(happyList)
    listList.append(sadList)
    listList.append(surpriseList)
    listList.append(neutralList)

    return listList

def graphData(subEmo):

    """
    TODO change a axit to seconds not frames
    TODO remove long straight lines between data points
    """

    print("Creating graph")
    frameList = []
    angryList = []
    disgustList = []
    fearList = []
    happyList = []
    sadList = []
    surpriseList = []
    neutralList = []

    for i in subEmo:
        frameList.append(subEmo[i]["frame"])
        angryList.append(subEmo[i]["angry"])
        disgustList.append(subEmo[i]["disgust"])
        fearList.append(subEmo[i]["fear"])
        happyList.append(subEmo[i]["happy"])
        sadList.append(subEmo[i]["sad"])
        surpriseList.append(subEmo[i]["surprise"])
        neutralList.append(subEmo[i]["neutral"])

    pointDensity = 2000

    x = np.linspace(min(frameList), max(frameList), pointDensity)

    angryListY = smooth(frameList, angryList, spacing=pointDensity)
    disgustListY = smooth(frameList, disgustList, spacing=pointDensity)
    fearListY = smooth(frameList, fearList, spacing=pointDensity)
    happyListY = smooth(frameList, happyList, spacing=pointDensity)
    sadListY = smooth(frameList, sadList, spacing=pointDensity)
    surpriseListY = smooth(frameList, surpriseList, spacing=pointDensity)
    neutralListY = smooth(frameList, neutralList, spacing=pointDensity)


    plt.plot(x, angryListY, "r", label = "anger") #Red
    plt.plot(x, disgustListY, "m", label = "disgust") #Magenta
    plt.plot(x, fearListY, "c", label = "fear") #Cyan
    plt.plot(x, happyListY, "g", label = "happy") #Green
    plt.plot(x, sadListY, "b", label = "sad") #Blue
    plt.plot(x, surpriseListY, "y", label = "surprise") #Yellow
    plt.plot(x, neutralListY, "k", label = "neutral") #Black

    plt.legend(loc="upper left")

    plt.ylim(0,100)

    print("Show graph")
    plt.show()

def smooth(x, y, spacing = 200, bc_type = "clamped"):

    """
    TODO New smooting algorithm that doesn't exceed the range 0-100
    """

    #define x as 200 equally spaced values between the min and max of original x 
    newX = np.linspace(min(x), max(x), spacing) 
    #define spline
    spl1 = make_interp_spline(x, y, k=3, bc_type=bc_type)
    newY = spl1(newX)

    return newY

def dominantEmotion(a_dict, output = 0):
    """
    output 0 = output to console
           1 = return list
           2 = return dominant emotion
    """

    #Turn dict into list
    a_list = dictToList(a_dict)

    #Find number of frames
    length = len(a_list[0])
    emoLength = 7

    dominantFrameEmotion = []

    #Check each value of data for each frame
    for frame in range(length):
        highestValue = 0
        highestEmotion = 0

        #Find the highest value and add it to the list
        for emotion in range(emoLength):

            if a_list[emotion][frame] > highestValue:
                highestEmotion = emotion
                highestValue = a_list[emotion][frame]

        dominantFrameEmotion.append(highestEmotion)
            # print(a_list[emotion][frame])
    
    emotionCountList = [0,0,0,0,0,0,0]

    for count in dominantFrameEmotion:
        emotionCountList[count] += 1

    emotionList = ["angry","disgust","fear","happy","sad","surprise","neutral"]
    
    #If output is set to 0, output to console
    if output == 0:
        for count in range(len(emotionCountList)):
            print(emotionList[count], ": ", emotionCountList[count])

    #If output is set to 1, return list
    if output == 1:
        return(emotionCountList)

    #If output is set to 2, retun most dominant emotion
    if output == 2:
        highestValue = 0
        highestEmotion = 0
        emotion = 0

        #Find highest emotion
        for count in emotionCountList:
            
            if count > highestValue:
                highestValue = count
                highestEmotion = emotion 
            
            emotion += 1
        
        return emotionList[highestEmotion]

def normaliseList(a_list):
    
    #Find lowest value
    lowestValue = min(a_list)

    #Divide all values by lowest
    for count in range(len(a_list)):
        a_list[count] = a_list[count]/lowestValue

    return(a_list)

def volumeEmotion(a_dict, normalize = False):
    a_list = dictToList(a_dict)

    totalEmotionList = []

    for data in a_list:
        totalEmotionList.append(sum(data))

    if normalize:
        return normaliseList(totalEmotionList)
    else:
        return totalEmotionList


