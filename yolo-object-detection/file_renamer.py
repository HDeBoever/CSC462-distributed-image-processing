# This script looks into the processed_split_images folder, and associates a prefix address to each file name based on the number in the file name


import sys, os, os.path, re
from os import listdir
from os.path import isfile, join


def rename_images(prefix1, prefix2, prefix3, prefix4, images_location):

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
			os.rename(dir_path + image, dir_path + prefix1 + image)
			print(prefix1  + image)
		elif int(number) <= 416:
			os.rename(dir_path + image, dir_path + prefix2 + image)
			print(prefix2  + image)
		elif int(number) <= 624:
			os.rename(dir_path + image, dir_path + prefix3 + image)
			print(prefix3  + image)
		elif int(number) <= 832:
			os.rename(dir_path + image, dir_path + prefix4 + image)
			print(prefix4  + image)

# program has to be passed the 4 prefix addresses on runtime
# Run the program with A_ B_ C_ D_
def main(argv):

	prefix1 = argv[1]
	prefix2 = argv[2]
	prefix3 = argv[3]
	prefix4 = argv[4]

	rename_images(prefix1, prefix2, prefix3, prefix4, 'split_images')

if __name__ == "__main__":
	main(sys.argv)
