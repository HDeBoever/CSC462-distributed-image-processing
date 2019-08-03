# This script will call yolo.py in a loop to process all the images in the split_images folder


import os, os.path, sys

docker_variable = os.getenv('ID')
print("docker var: " + docker_variable)

images = [f for f in listdir('split_images') if isfile(join('split_images', f))]
images.sort(key = lambda x: int(''.join(filter(str.isdigit, x))))

curr_file_number = 0
for filename in images:

	prefix = filename[:2]
	if docker_variable == filename[0]:
		os.system('python yolo.py --image split_images/' + prefix + 'airport' + str(curr_file_number + 1) +'.jpg --yolo yolo-coco')
	else:
		continue

	curr_file_number += 1
