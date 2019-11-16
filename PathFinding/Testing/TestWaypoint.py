# Date - 11/15/19
# Contributers:
    # Patrick Sacchet (pjsacchet)

import unittest
import sys
sys.path.append("..")

from Waypoint import Waypoint

class TestWaypoint(unittest.TestCase):

    def test_init(self):
        waypoint = Waypoint(1, 2, 3)
        self.assertTrue(waypoint.__class__ == Waypoint and waypoint.x_cord == 1 and waypoint.y_cord == 2 and
        waypoint.z_cord == 3)

    def test_str(self):
        waypoint = Waypoint(1, 2, 3)
        self.assertTrue(waypoint.__str__() == ("These are my x, y and z coordinates: 1 2 3" + "\n"))

    def test_set_x_coordinate(self):
        waypoint = Waypoint(1, 2, 3)
        waypoint.set_x_cord(2)
        self.assertTrue(waypoint.x_cord == 2)

    def test_set_y_coordinate(self):
        waypoint = Waypoint(1, 2, 3)
        waypoint.set_y_cord(1)
        self.assertTrue(waypoint.y_cord == 1)

    def test_set_z_coordinate(self):
        waypoint = Waypoint(1, 2, 3)
        waypoint.set_z_cord(2)
        self.assertTrue(waypoint.z_cord == 2)

if __name__ == '__main__':
    unittest.main()
