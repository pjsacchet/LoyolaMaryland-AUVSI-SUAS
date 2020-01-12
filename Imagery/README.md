# Image Recognition

## File Breakdown:

### DetectColor.py:

### ProcessShapes.py:
Takes images as input using command line interface.  Once image is enterted, it is then resizes it and blurs it slightly.  Image is then refactored to compute the center of contour points.  Contour lines are then displayed, as well as name of the image (if this ran).
 // $ python ProcessShapes.py --image test_img_1.png

### ReduceNoise.py:

### ShapeDetector.py:
https://www.khanacademy.org/math/geometry-home/geometry-shapes/geometry-curves-and-polygons/v/intro-to-curves-basic-geometrical-ideas-class-6-india-khan-academy - Curve explanation

Shape detector takes in a variable c, the curve, and then determines the shape. The shape is determined by the amount of curves. Don't let the name mislead you, a curve can be a straight line or curved.

## TODO:
* Develop plan for better integrating old code into new layout
* Read for better understanding the API of the modules imported
* Implement testing commands via CMD line via subprocessing (Patrick can do this)
