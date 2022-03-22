import functions as f
import os

# File locations
img_directory = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis"
name = "split_0_data"

path = os.path.join(img_directory, name)

d = f.loadData(directory=path)

# print(d)

l = f.dataToList(data=d)
print(l)
