import matplotlib.pyplot as plt
import json
# from matplotlib.pyplot import figure

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

def getSegmentValues(data):
    
    dataValueList = data
    i = 0

    while i < len(dataValueList)-1:
        if dataValueList[i] == dataValueList[i+1]:
            del dataValueList[i]
        else:
            i = i+1
    
    return dataValueList

def getSegments(data):
    segments = [0]
    segmentElement = data[0]
    
    for index in range(len(data)):
        
        if data[index] != segmentElement:
            
            segments.append(index - 1)
            segmentElement = data[index]

    segments.append(len(data)-1)
    
    return segments

def graph1D(segmentSpacingList, segmentValuesList, dataNameList):

    key = ["r","m","c","g","b","y","k"]
    tickPos = []


    for dataSet in range(len(segmentSpacingList)):
        tickPos.append(dataSet)
        for segment in range(len(segmentSpacingList[dataSet]) - 1):
            print(segmentSpacingList[dataSet][segment], segmentSpacingList[dataSet][segment + 1], segmentValuesList[dataSet][segment])
            seg = segmentSpacingList[dataSet][segment], segmentSpacingList[dataSet][segment + 1]
            y = [dataSet, dataSet]

            if segmentValuesList[dataSet][segment] != 0:
                plt.plot(seg, y, key[segmentValuesList[dataSet][segment]-1], linewidth=20)

    plt.yticks(tickPos, dataNameList)
    plt.xlim(0, max(segmentSpacingList[0]))
   
    plt.show()