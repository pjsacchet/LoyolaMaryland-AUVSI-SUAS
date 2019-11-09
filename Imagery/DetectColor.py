# import the necessary packages
import numpy as np
import argparse
import cv2 #opencv

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser() #take in arguments and parses them
ap.add_argument("-i", "--image", help = "path to the image") #adds image with arguments similar to a cli
args = vars(ap.parse_args()) #vars returns attribute of the _dict_ attribute of module,class, instance, and or any object with the same _dict_ attribute

# load the image
image = cv2.imread(args["image"]) #functionality of the open cv -- take in image as an argument

# define the list of boundaries
boundaries = [
	([0, 0, 144], [162,162,255]),  		#red
	([150,0,26], [255,150,150]),   		#blue
	([0, 128, 128], [100, 255, 255]), 	#yellow
	([64, 64, 64], [217, 217, 217])   	#gray
]
#These are rgb value boundaries for different colors^

i = 0
# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8") # just creates arrays with images
	upper = np.array(upper, dtype = "uint8") #The images are represented like numpy arrays 

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper) #parameters:the pic, lower limit of color boundary, higher limit of color boundary ---its the actual color detection
	# a binary mask is returned (white pixels(255) represent pixels that fall into the upper and lower bounds and black pixels dont
	output = cv2.bitwise_and(image, image, mask = mask) #the output image -shows only the pixels in the "image" that correspond with the white(255) value in the mask

	# show the images
	cv2.imshow("images", np.hstack([image, output])) #this is similar to a printout but in image form
	#cv2.imshow("images", output)
	name = "test_img_" + str(i) + ".png"

	cv2.imwrite(name, output)
	cv2.waitKey(0)
	i = i + 1
