# Date - 11/15/19
# Contributers:
    # Patrick Sacchet (pjsacchet)

from sys import *
from os import *
from datetime import date

from Waypoint import Waypoint


# Class will serve to create file parser objects specific to competition input files, can parse input files and format them to output to output file
class WaypointParser:


    # Constructor for a waypoint parser object
    # Input: file_loc - location of file to be parsed
    # Returns: None
    def __init__(self, file_loc, output_filename):
        self.file_loc = file_loc
        date = date.now()
        # Create and assign a new output file with date and time created, then create the file in the directory 
        self.output_filename = date + ".txt"
        output_file = open(self.output_filename, "w")
        close(self.output_filename)
        return

    # Parses the file passed to create waypoint objects
    # Input: None
    # Returns: waypoints - array of waypoint objects ready to be formatted in output file
    def parse_file(self):
        # Parse through file until reaching '<Waypoints>' tag in .kml
        # Check that file actually exists, if not print error and return
        if(!os.path.exists(self.file_loc)):
            print("File location doesn't exist bud, try again \n")
            return
        # Else, file actually exists so lets get started
        else:
            # Initialize list of waypoint objects
            waypoints = []
            pass
