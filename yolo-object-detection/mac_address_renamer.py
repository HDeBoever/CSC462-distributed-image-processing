# This script looks into the processed_split_images folder, and associates a MAC address to each file name based on the number in the file name


import sys, os, os.path, re
from os import listdir
from os.path import isfile, join


def rename_images(mac1, mac2, mac3, mac4, images_location):

	images_to_be_renamed = [f for f in listdir(images_location) if isfile(join(images_location, f))]
	images_to_be_renamed.sort(key = lambda x: int(''.join(filter(str.isdigit, x))))
	print(images_to_be_renamed)

	for image in images_to_be_renamed:
		print(image)
		dir_path = os.path.dirname(os.path.realpath(image))
		dir_path = dir_path + '\\' + images_location + '\\'
		print(dir_path)
		curr_image_number = (re.findall('\d+', str(image)))
		number = curr_image_number[0]

		if int(number) <= 208:
			os.rename(dir_path + image, dir_path + mac1 + image)
			print(mac1  + image)
		elif int(number) <= 416:
			os.rename(dir_path + image, dir_path + mac2 + image)
			print(mac2  + image)
		elif int(number) <= 624:
			os.rename(dir_path + image, dir_path + mac3 + image)
			print(mac3  + image)
		elif int(number) <= 832:
			os.rename(dir_path + image, dir_path + mac4 + image)
			print(mac4  + image)

# program has to be passed the 4 mac addresses on runtime
def main(argv):

	mac1 = argv[1]
	mac2 = argv[2]
	mac3 = argv[3]
	mac4 = argv[4]

	# pass in the mac addresses of the 4 nodes in the form "000000000001"
	# and the name of the directory where the target images are
	rename_images(mac1, mac2, mac3, mac4, 'split_images')

if __name__ == "__main__":
	main(sys.argv)
