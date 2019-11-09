# import the necessary packages
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	#According to opencv API
	#https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=approxpolydp#cv2.approxPolyDP
	#approxPolyDP(c,epsilon,Closed)
	# c (curve) - input vector of a 2D point stored in a numpy array
	#0.04 * peri -(epsilon – Parameter specifying the approximation accuracy. This is the maximum distance between the original curve and its approximation.
	#Truse (closed -If true, the approximated curve is closed (its first and last vertices are connected).)
	#The functions approxPolyDP approximate a curve or a polygon with another curve/polygon with less vertices so that the distance between them is less or equal to the specified precision. It uses the Douglas-Peucker algorithm http://en.wikipedia.org/wiki/Ramer-Douglas-Peucker_algorithm
	#Detects what the shape is
	def detect(self, c):
		# initialize the shape name and approximate the contour
		shape = "unidentified"
		peri = cv2.arcLength(c, True)
		approx = cv2.approxPolyDP(c, 0.04 * peri, True)

		##Print to see the output of this
		printf("Approx = " approx)

		# if the shape is a triangle, it will have 3 vertices
		if len(approx) == 3:
			shape = "triangle"

		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif len(approx) == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx) #CV2 - The function calculates and returns the minimal up-right bounding rectangle for the specified point set.
			ar = w / float(h)

			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"

		# if the shape is a pentagon, it will have 5 vertices
		elif len(approx) == 5:
			shape = "pentagon"

		elif ( len(approx) > 5 ) and ( len(approx) <= 10 ) :
			shape = ( "star " + str(len(approx)) )

		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"

		# return the name of the shape
		return shape
