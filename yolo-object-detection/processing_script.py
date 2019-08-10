# This script will call yolo.py in a loop to process all the images in the split_images folder


import os, os.path, sys

docker_variable = os.getenv('ID')
print("docker var: " + docker_variable)

for filename in os.listdir('split_images'):

	prefix = filename[:2]
	# A_airport____.jpg
	file_number = [9:-4]
	if docker_variable == filename[0]:
		os.system('python yolo.py --image split_images/' + prefix + 'airport' + str(file_number) +'.jpg --yolo yolo-coco')
	else:
		continue
