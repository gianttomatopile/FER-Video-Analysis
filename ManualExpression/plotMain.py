import plottingFunctions as pf
"""
Shows the dominant emotions as two datasets
"""

#Data directories
comData = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Complete_data"

#Load data
data_C = pf.loadData(comData)

#Create the data segments and their corrisponding values
data_C_segments = pf.getSegments(data_C)
data_C_values = pf.getSegmentValues(data_C)

#With multiple datasets must be added to a list
segmentLists = []
segmnetValuesList = []

segmentLists.append(data_C_segments)
segmnetValuesList.append(data_C_values)

#Name for each dataset
dataNames = ["Complete Data"]

#plot data
pf.graph1D(segmentLists, segmnetValuesList, dataNames)
