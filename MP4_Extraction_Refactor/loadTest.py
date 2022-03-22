import emotionExtractionFunctions as eef
import os

#File locations
img_directory = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\MP4_Extracted"
name = "QuckFace_subEmo.json"

path = os.path.join(img_directory, name)

subEmoOut = eef.loadData(path)

# print(subEmoOut)
eef.graphData(subEmo=subEmoOut)