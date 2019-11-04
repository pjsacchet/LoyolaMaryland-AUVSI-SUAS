import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

#blur = cv2.bilateralFilter(img,9,75,75)
blur = cv2.medianBlur(img,5)

cv2.imwrite("filtered.png", blur)
