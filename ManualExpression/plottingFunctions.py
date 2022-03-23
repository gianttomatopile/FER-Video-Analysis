from itertools import count
from operator import index
from turtle import color
import matplotlib.pyplot as plt
import json
import pickle
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

    segments = []
    segmentElement = data[0]
    
    segment_start = 0
    segment_end = 0
    tempSegment = [segment_start, segment_end]
    
    for index in range(len(data)):
        
        if data[index] != segmentElement:

            #Close statement
            segment_end = index - 1
            #Update temp segment
            tempSegment = [segment_start, segment_end]

            #Add to segment list
            segments.append(tempSegment)

            #open new segment
            segment_start = index

            #Assign new segment value
            segmentElement = data[index]

    #Get point of last frame
    segment_end = len(data) - 1
    #Update temp segment
    tempSegment = [segment_start, segment_end]
    #Add end of last segment
    segments.append(tempSegment)
    
    return segments

def graph1D(segmentSpacingList, segmentValuesList, dataNameList, save=False, name="plot"):
    """
    Plot horizontal bars representing the dominant emotion of multiple datasets
    """
    #Assign a colour for each emotion number
    key = ["r","m","c","g","b","y","k"]

    #Count the number of data sets
    tickPos = []

    #Go through each individual dataset
    for dataSet in range(len(segmentSpacingList)):
        
        #Count up
        tickPos.append(dataSet)
        
        #For each segment in dataset
        for segment in range(len(segmentSpacingList[dataSet]) - 1):

            # print(segmentSpacingList[dataSet][segment], segmentSpacingList[dataSet][segment + 1], segmentValuesList[dataSet][segment])
            

            x = [segmentSpacingList[dataSet][segment][0], segmentSpacingList[dataSet][segment][1]]
            y = [dataSet, dataSet]

            if segmentValuesList[dataSet][segment] != 0:
                plt.plot(x, y, key[segmentValuesList[dataSet][segment]-1], linewidth=2)

    plt.yticks(tickPos, dataNameList)
    # plt.xlim(0, max(segmentSpacingList[0]))


    if save:
        plt.savefig(name)

    plt.show()

def bar_segment_data(data):
    segments = []
    element = data[0]

    for index in range(len(data)):
        
        if data[index] != element:
            segments.append(index - 1)
            element = data[index]

    segments.append(len(data) - 1)
    return segments

def bar_segment_value_data(data):
    values = [data[0]]

    last_element = data[0]

    for element in data:
        if element != last_element:
            values.append(element)
            last_element = element

    return values

def bar_plot(segments_list, values_list, name_list):

    key = ["r","m","c","g","b","y","k"]
    value_count = 0

    for data_set in segments_list:

        item_count = 0
        
        for segment in data_set:
            
            print(values_list[value_count][item_count])

            plt.bar(name_list, 
                    segment,
                    bottom = 0, 
                    color = key[values_list[value_count][item_count] - 1])
            
            item_count += 1
        
        value_count += 1
    
    plt.show()

