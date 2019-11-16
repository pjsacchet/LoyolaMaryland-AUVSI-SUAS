# Import the necessary packages
#from pyimagesearch.shapedetector import ShapeDetector
from ShapeDetector import ShapeDetector
# Allows the user to use command line interface
import argparse
# Allows image processing for translating, rotation, resizing, displaying etc.
import imutils
# Software allows computer vision and machine learning
import cv2
import pdb

#def main():
  ## Input: image file
   # Output: None
   # Purpose: Reads the image to see if it exists
  ##
  # ArgumentParser() turns the argument value from a string to an object
  def takingImage():
    ap = argparse.ArgumentParser()
    # Taking a string from user and turning it into an object
    ap.add_argument("-i", "--image", required=True, help="path to the input image")
    args = vars(ap.parse_args())

  ## Input: None
   # Output: None
   # Purpose: Load the image and resize it to a smaller factor so that
   # the shapes can be approximated better
  ##
  # Returns a NumPy array representing the image
  def processImage():
    image = cv2.imread(args["image"])
    # Image being rezied
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])

  ## Input: None
   # Output: None
   # Purpose: Converts the resized image to grayscale, blur it slightly,
   # and threshold it
  ##
  def refaction(resized):
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

  ## Input:None
   # Output: None
   # Purpose: Find contours in the thresholded image and initialize the
   # shape detector
  ##
  # thresh.copy() is source image, cv2.RETR_EXTERNAL is contour retrieval mode,
  # cv2.CHAIN_APPROX_SIMPLE is contour approximation method
  # Essentially stores the (x,y) coordinates of the boundary of a shape
  def findCordinates(cnts):
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()

  ## Input: Name of an image
   # Output: None
   # Purpose: loop over the contours
  ##
  def computeContour(cnts):
    for c in cnts:
      # Compute the center of the contour, then detect the name of the
      # shape using only the contour
      M = cv2.moments(c)
      cX = int((M["m10"] / M["m00"]) * ratio)
      cY = int((M["m01"] / M["m00"]) * ratio)
      shape = sd.detect(c)

    # Multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image

      c = c.astype("float")
      c *= ratio
      c = c.astype("int")
      cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
      cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 255, 255), 2)

  def displayImage(image):
    # Displays the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
  return image


if __name__ == "__main__":
  main()
  takingImage()

# Do we care about what the letter is
# Break up code into functions
# Find out why image 3 is not loved