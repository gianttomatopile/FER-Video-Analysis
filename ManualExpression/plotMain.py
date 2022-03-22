import plottingFunctions as pf

split_0 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Split_0_data"
split_1 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Split_1_data"

data_0 = pf.loadData(split_0)
data_1 = pf.loadData(split_1)

# print(data_0)
data_0_segments = pf.getSegments(data_0)
data_0_values = pf.getSegmentValues(data_0)

data_1_segments = pf.getSegments(data_1)
data_1_values = pf.getSegmentValues(data_1)

segmentLists = []
segmnetValuesList = []

segmentLists.append(data_0_segments)
segmnetValuesList.append(data_0_values)
segmentLists.append(data_1_segments)
segmnetValuesList.append(data_1_values)

dataNames = ["Data set 0", "Data set 1"]

# segmentLists.append(data_0_segments)
# segmnetValuesList.append(data_0_values)

# dataNames = ["D1", "D2", "D3"]

pf.graph1D(segmentLists, segmnetValuesList, dataNames
)

# print(segmentLists)
# print(segmnetValuesList)