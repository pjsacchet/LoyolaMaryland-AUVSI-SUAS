# Date - 11/15/19
# Contributers:
    # Patrick Sacchet (pjsacchet)

import sys
import os

# Class represents a waypoint given in the competition. Funcitonality will allow user to manipulate input given via command line
class Waypoint:

    # Constructor for a waypoint object
    # Input:
        # x_cord - x coorindate of the waypoint
        # y_cord - y cooridnate of the waypoint
        # z_cord - z coorindate of the waypoint
    def __init__(self, x_cord, y_cord, z_cord):
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.z_cord = z_cord
        return

    # Simple print statement conversions
    # Input: None
    # Returns: String with x y and z coordinates
    def __str__(self):
        str_coord = "These are my x, y and z coordinates: " + str(self.x_cord) + " " + str(self.y_cord) + " " + str(self.z_cord) + "\n"
        return str_coord

    # Sets new x coordinate
    # Input: x_cord - new x coordinate
    # Returns: None
    def set_x_cord(self, x_cord):
        self.x_cord = x_cord
        return

    # Sets new y coordinate
    # Input: y_cord - new y coordinate
    # Returns: None
    def set_y_cord(self, y_cord):
        self.y_cord = y_cord
        return

    # Sets new z coordinate
    # Input: z_cord - new z coordinate
    # Returns: None
    def set_z_cord(self, z_cord):
        self.z_cord = z_cord
        return
