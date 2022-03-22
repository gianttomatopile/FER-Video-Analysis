import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline
import emotionExtractionFunctions as eef
import os


def listData(a_dict):
    frameList = []
    dataLists = [[],[],[],[],[],[],[]]

    for i in a_dict:
        frameList.append(a_dict[i]["frame"])
        dataLists[0].append(a_dict[i]["angry"])
        dataLists[1].append(a_dict[i]["disgust"])
        dataLists[2].append(a_dict[i]["fear"])
        dataLists[3].append(a_dict[i]["happy"])
        dataLists[4].append(a_dict[i]["sad"])
        dataLists[5].append(a_dict[i]["surprise"])
        dataLists[6].append(a_dict[i]["neutral"])
    
    return frameList, dataLists

def splitGraph(frameList, dataList, gapSize = 2):
    frameLists = []
    dataLists = []
    sectionFrameList = []
    sectionDataList = []

    for count in range(len(frameList)):
        
        #get frame number
        frame = frameList[count]

        #Check if first frame
        if count == 0:
            preFrame = frameList[count]
        else:
            preFrame = frameList[count - 1]

        #Get boundary frame number
        # print("preframe", preFrame, count)
        boundaryFrame = preFrame + gapSize

        #Check if next frame exceeds boundary
        if frame > boundaryFrame:
            frameLists.append(sectionFrameList)
            sectionFrameList = []
            sectionFrameList.append(frameList[count])

            #Add all data here
            dataLists.append(sectionDataList)
            sectionDataList = []
            sectionDataList.append(dataList[count])
        else:
            #Add to lists
            sectionFrameList.append(frameList[count])
            sectionDataList.append(dataList[count])

    #Add final list
    frameLists.append(sectionFrameList)
    dataLists.append(sectionDataList)

    # return dataLists
    return dataLists, frameLists

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

def unused():
    frameList = [0,1,2,3,6,7,9,12,13,14,15]
    dataList1  = [1,2,3,4,5,6,7,8,9,10,11]
    dataList2 = [2,3,5,7,9,2,3,5,7,11,10]

    fr, dl1 = splitGraph(frameList, dataList1, gapSize = 1)
    # fr, dl2 = splitGraph(frameList, dataList2, gapSize = 1)

    smoothedDataLists = []
    smoothedFrameList = []

    for count in range(len(fr)):

        if len(fr[count]) == 1:
            smoothedDataLists.append(dl1[count])
            smoothedFrameList.append(fr[count])
        else:
            print(fr[count])
            print(dl1[count])
            spacing = len(fr[count])*10
            smoothList = smooth(fr[count],dl1[count], spacing=spacing)
            smoothedDataLists.append(smoothList)

            smoothedFrameList.append(np.linspace(min(fr[count]), max(fr[count]), spacing))

    # print(dl1[0])    
    # print(smoothedDataLists[0])
    # print(smoothedFrameList[0])
    print("----------------------------------------------------")
    # For each sengment of list either plot a dot or line depending on length
    for i in range(len(smoothedFrameList)):
        print(smoothedDataLists[i])
        print(smoothedFrameList[i])
        if len(smoothedFrameList[i]) == 1:
            plt.plot(smoothedFrameList[i], smoothedDataLists[i], color='blue', marker='o', markersize=2)
        else:
            plt.plot(smoothedFrameList[i], smoothedDataLists[i], "b", linewidth = 2)

    plt.show()

def main():

    #File location
    img_directory = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\MP4_Extracted"
    name = "QuckFace_subEmo.json"
    #Create path
    path = os.path.join(img_directory, name)
    #Load dict
    subEmoOut = eef.loadData(path)
    #Turn into all lists
    frameList, dataLists = listData(subEmoOut)

    splitDataLists = [[],[],[],[],[],[],[]]

    #For each list of data split it up
    for i in range(len(splitDataLists)):
        splitDataLists[i], splitFrameList = splitGraph(frameList=frameList, dataList=dataLists[i])

    print(splitFrameList)
    print(splitDataLists)

    for data in splitDataLists:
        frames = splitFrameList

# main()
unused()