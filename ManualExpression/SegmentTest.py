import plottingFunctions as pt
import matplotlib as plt

data1 = [1,1,1,1,2,2,2,3,3,4,1,1,1]
data2 = [2,2,2,2,3,3,1,1,4,4,4,1,1]


seg_data_1 = pt.bar_segment_data(data1)
# print(pt.bar_segment_data(data2))

seg_values_1 = pt.bar_segment_value_data(data1)

print(seg_data_1)
print(seg_values_1)

seg_list = []
seg_list.append(seg_data_1)

value_list = []
value_list.append(seg_values_1)

# pt.bar_plot(segments_list=seg_list, values_list=value_list, name_list=["d1"])

# d1 = pt.getSegments(data1)
# d2 = pt.getSegments(data2)

# print(d1,d2)