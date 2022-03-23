import cv2
import json
import os

def frameByFrameStep(vid_source, dir, name):
    """
    Steps through a video frame-by-frame and allows the user to 
    input their analysis of the dominant emotion 
    1 = angry
    2 = disgust
    3 = fear
    4 = happy
    5 = sad
    6 = surprised
    7 = netral
    q = quit
    space = skip frame

    vid_source = directory for video 
    dir = directory for where to save data
    name = name to save the data as

    returns a list of data
    """
    data = []

    cap = cv2.VideoCapture(vid_source)

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`

    scale = 0.5

    newWidth = int(scale * width)
    newHeight = int(scale * height)

    print('width, height:', width, height)

    run = True

    while run == True:
        acceptKey = False

        #capture frame
        ret, frame = cap.read()
        
        quit = False
        
        #Break loop if end of no frame
        if ret == False:
            break

        im2 = cv2.resize(frame, (newWidth, newHeight)) 
        cv2.imshow("window", im2)

        while acceptKey == False:

            res = cv2.waitKey(0)

            for count in range(1,8):
                if res == ord(str(count)):
                    data.append(int(chr(res)))
                    acceptKey = True
                    break           
                     
            if res == ord("q"):
                #If q pressed save and quit
                storeData(element=data,directory=dir,name=name)
                
                print("break")
                quit = True
                acceptKey = True
            
            if res == ord(" "):
                #If space pressed move on to next frame
                data.append(0) #Zero represents a skipped frame
                acceptKey = True            
            
            if not(acceptKey):
                print("Input invalid:", chr(res))
            
            
        
        if quit == True:
            break


    cap.release()

    storeData(element=data,directory=dir,name=name)
    return data

def dataToList(data):
    a_list = [[],[],[],[],[],[],[]]

    r = range(1,8)
    for count in range(len(data)):
        for i in r:
            # print(i, count, data[count])
            if i == data[count]:
                a_list[i-1].append(count)

    return a_list

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

