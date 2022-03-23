import functions as f
"""
Used to run the frame-by-frame manual analysis
"""
  
split_0 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_0.mp4"
split_1 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_1.mp4"
split_2 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_2.mp4"
split_3 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_3.mp4"
split_4 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_4.mp4"
split_5 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_5.mp4"
split_6 = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis\Video splices\Split_6.mp4"
dir = r"C:\Users\Willi\OneDrive\Desktop\Manual_data_analysis"

name = "Split_6_data"
print(f.frameByFrameStep(vid_source=split_6, 
                         dir=dir, 
                         name=name))

