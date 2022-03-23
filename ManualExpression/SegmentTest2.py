from tkinter import BOTTOM
import plottingFunctions as pt
import matplotlib.pyplot as plt
import numpy as np

# d0 = [1,1,1,2]
# d1 = [4,3,2,1,6]
# d2 = [2,3,5]

# data = [d0, d1, d2]


# #define the function#
# def find_max_list(list):
#     list_len = [len(i) for i in list]
#     return max(list_len)

# #print output
# longest_list_length = find_max_list(data)

# rot_list = [[]] * longest_list_length

# for count in range(longest_list_length):
#     # print(count)
#     print("---------")
#     index = 0



#     for d in data:
#         # print(len(d), count)
#         if len(d) <= count:
#             print("0")
#             rot_list[index].append(0)
#         else:
#             print(d[count])
#             rot_list[index].append(d[count])
#         print("index:", index)

#         index += 1
    
#     # rot_list[count].append(data[count])
    
# print(rot_list)

#######################

# layer0 = np.array([3, 2])
# layer1 = np.array([5, 3])
# layer2 = np.array([2, 0])

# name = ["test1", "test2"]

# plt.bar(name, layer0)
# plt.bar(name, layer1, bottom = layer0)
# plt.bar(name, layer2, bottom = (layer0 + layer1 + 1))

# name2 = ["test3", "test4"]

# plt.bar(name2, layer0)
# plt.bar(name2, layer1, bottom = layer0)
# plt.bar(name2, layer2, bottom = (layer0 + layer1 + 1))

# plt.show()

data = [1,2,5,2,4,1,3]
bot = 0
bar1 = "bar1"

for inx in data:
    plt.bar(bar1, inx,bottom=bot)
    print(inx)
    bot += inx

data2 = [1,2,5,2,4,1,3]
bot2 = 0
bar2 = "bar2"

for inx in data2:
    plt.bar(bar2, inx,bottom=bot2)
    print(inx)
    bot2 += inx

plt.show()