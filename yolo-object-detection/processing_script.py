# This script will call yolo.py in a loop to process all the images in a given folder


import os, os.path, sys

docker_variable = sys.argv[1]
print(docker_variable)

for filename in os.listdir('split_images'):
	curr_file_number = 0

	prefix = filename[:2]
	if docker_variable == filename[0]:
		os.system('python yolo.py --image split_images/' + prefix + 'airport' + str(curr_file_number + 1) +'.jpg --yolo yolo-coco')
	curr_file_number += 1
