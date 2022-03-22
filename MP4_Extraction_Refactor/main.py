import emotionExtractionFunctions as eef

#Subject file
sub_photo = (r"\subject_1.0.jpg", #Will1
             r"\subject_1.1.jpg", #Will2
             r"\subject_1.2.jpg", #Will3
             r"\subject_1.3.jpg", #Will4
             r"\subject_2.0.jpg", #Emily1
             r"\subject_2.1.jpg", #Emily2
             r"\subject_3.0.jpg") #Audrie H.

# File names
vid_file = (r"\Test_Data_Short.mp4", #subject_1
            r"\Test_Data_Long.mp4", #subject_1
            r"\big_buck_bunny_720p_5mb.mp4", #NO SUBJECT
            r"\Test_Data_VeryShort.mp4", #subject_1.1
            r"\Test_Data_Two_People_Short.mp4", #subject_1.2
            r"\Test_Data_Smile.mp4", #subject_1.1
            r"\Emily_Happy.mp4", #subject_2.1
            r"\Four_People.mp4", #UNGENERATED
            r"\Charade (1963) (25.14 to 31.43).mp4") #subject_3.0

#File locations
vid_source = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\MP4_Videos" + vid_file[5]
sub_source = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\MP4_Subject" + sub_photo[3]
img_directory = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\MP4_Extracted"
subject_directory = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\Subject_faces"

#group test source
# sub_source = r"C:\Users\Willi\OneDrive\Desktop\Christmas Work\Test_Scripts_Backup\FER_Test_Code\Test_Scripts\MP4_Subject\subject_group_1" 

imageList = eef.quickAnalysis(vid_source=vid_source,
                              img_directory=img_directory)

DFImages = eef.detailedAnalysis(imageList=imageList, 
                                img_directory=img_directory)


subImages = eef.contiuity(DFImages=DFImages, 
                          img_directory=img_directory,
                          sub_source=sub_source)

subEmo = eef.emotionDetection(subImages=subImages, img_directory=img_directory)

name = "QuckFace_subEmo.json"
eef.storeData(element=subEmo,directory=img_directory, name=name)

eef.graphData(subEmo=subEmo)

"""
TODO add importance of emotion by portion of screen taken up by face
TODO john.mateer
"""