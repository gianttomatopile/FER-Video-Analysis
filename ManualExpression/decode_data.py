import functions as f

"""
Combines all the splits of data into one list that's saved
"""

data = []

for i in range(0,7):
    # print(i)
    path = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Split_" + str(i) + "_data"
    data = data + f.loadData(path)


print(data)

name = "Complete_data"
dir = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis"
f.storeData(data,dir, name)

