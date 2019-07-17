# ------------------------------------------------------------------------------
# Images (Frames) to Video
# Using this code we can generate video from Images (Frames). We have to add pathIn (path of the folder
# which contains all the images). I set framerate with 0.5 so it will take 2 images for 1 second.)
# It will generate output video in any format. (eg.: .avi, .mp4, etc.)
# !!! Please take care that all images are in sequence like image1.jpg, image2.jpg and so on.


import cv2
import numpy as np
import os
from os.path import isfile, join

if not os.path.exists('recombined_videos'):
    os.makedirs('recombined_videos')

pathIn= './split_images/'
pathOut = './recombined_videos/video.avi'
fps = 0.5  # 4 frames per second
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
files.sort(key = lambda x: x[5:-4])
files.sort()
frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
files.sort(key = lambda x: int(''.join(filter(str.isdigit, x))))
print(files)
for i in range(len(files)):
    filename=pathIn + files[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)

    #inserting the frames into an image array
    frame_array.append(img)
out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
