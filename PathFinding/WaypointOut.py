# This file serves as a 'tie together' for waypoint parsing of judge data
# Date: 11/8/19
# Contributers:
    # Patrick Sacchet (pjsacchet)

import sys
import os
from pathlib import Path

from Waypoint import Waypoint
from WaypointParser import WaypointParser

# File functinality (reliant on last year's experience)
    # Ask how many waypoints there are to input
    # For each waypoint, create the standard 16 fields, but require input for the three given in the competition
        # Do this via string concated to formatted input

# Main functionality
def main():
    # Take in file location from user
    # Create file parser object out of it
    # Call parse_file()
        # Go through line by line until <coordinate> tag
        # Go to next line, set line delimiter to ','
        # For each three, create waypoint object and add to array of waypoint objects
        # Print leading zeros and then call string function to concat to end of line
    print("Testing...")
    p1 = Waypoint(1,2,3)
    print(p1)
    waypoint_parser_real = WaypointParser("SampleInput.py")
    waypoint_parser_real.parse_file()
    return 0;

if __name__ == "__main__":
    main()
