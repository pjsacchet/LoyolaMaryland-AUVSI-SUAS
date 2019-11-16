# Class represents a waypoint given in the competition. Funcitonality will allow user to manipulate input given via command line
# Date - 11/15/19
# Contributers:
    # Patrick Sacchet (pjsacchet)

import sys
import os

class Waypoint:

    def __init__(self):
        self.waypoint = 0
        return

    def __str__(self):
        str_coord = "This is my x coordinate: " + str(self.waypoint)
        return str_coord
