# https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481

# Video to Image (Frames) conversion

# In cv2.VideoCapture(‘video.mp4’), we just have to mention the video name with it’s extension.
# Here my video name is “video.mp4”. You can set frame rate which is widely known as fps (frames per second).
# Here I set 0.5 so it will capture a frame at every 0.5 seconds, means 2 frames (images) for each second.
# It will save images with name as image1.jpg, image2.jpg and so on.


import cv2
import sys, os
# vidcap = cv2.VideoCapture('videos/airport.mp4')
def getFrame(sec, video, count):
    video.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = video.read()
    if hasFrames:
        cv2.imwrite("split_images/image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

# main can be used to pass parameters to the functions below
# navigate to directory where ths file is located
# python video_splitter.py <path to video/videoName.mp4>
# this program will create the directory 'split_images' to store the output of the processed images
def main():
    if not os.path.exists('split_images'):
        os.makedirs('split_images')
    video = cv2.VideoCapture(sys.argv[1])
    sec = 0
    frameRate = 0.25 #//it will capture image in each 0.25 second
    count = 1
    success = getFrame(sec, video, count)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec, video, count)

if __name__ == "__main__":
   main()
