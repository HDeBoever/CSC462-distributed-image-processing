# This script will call yolo.py in a loop to process all the images in a given folder


import os, os.path


path, dirs, files = next(os.walk("split_images"))
file_count = len(files)
print(file_count)

for i in range (0, file_count):
	os.system('python yolo.py --image split_images/paris' + str(i + 1) +'.jpg --yolo yolo-coco')
