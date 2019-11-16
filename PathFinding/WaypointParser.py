# Date - 11/15/19
# Contributers:
    # Patrick Sacchet (pjsacchet)

import os
import os
from datetime import datetime
import pdb

from Waypoint import Waypoint


# Class will serve to create file parser objects specific to competition input files, can parse input files and format them to output to output file
class WaypointParser:

    # Constructor for a waypoint parser object
    # Input: file_loc - location of file to be parsed
    # Returns: None
    def __init__(self, file_loc):
        self.file_loc = file_loc
        date_curr = datetime.now()
        dt_str = date_curr.strftime("%d-%m-%Y_%H:%M:%S")
        # Create and assign a new output file with date and time created, then create the file in the directory
        self.output_filename = dt_str + ".txt"
        output_file = open(self.output_filename, "w")
        output_file.close()
        return

    # Write a line to our output file
    # Input: output_str - string of data for a waypoint to be printed to output file
    # Returns: None
    def write_file(self, output_str):
        print(output_str)
        # Open the output file for appending
        output_file = open(self.output_filename, "a")
        # Write the string and close the file
        output_file.write(output_str)
        output_file.close()
        return

    # Parses the file passed to create waypoint objects
    # Input: None
    # Returns: waypoints - array of waypoint objects ready to be formatted in output file
    def parse_file(self):
        # Parse through file until reaching '<Waypoints>' tag in .kml
        # Check that file actually exists, if not print error and return
        if(os.path.exists(self.file_loc) == False):
            print("File location doesn't exist bud, try again \n")
            return
        # Else, file actually exists so lets get started
        else:
            # Initialize list of waypoint objects
            waypoints = []
            coordinates_list = []
            # Open the file and begin to iterate over data, with each waypoint created, write to the output file
            input_file = open(self.file_loc, "r")
            # For each line in the file...
            for line in input_file:
                # If the line contains the coordinates tag...
                if("coordinates" in line):
                    # Get rid of the start and end tags, then set delimiters and create waypoint objects
                    pdb.set_trace()
                    line = line.replace('<coordinates>', '')
                    line = line.replace('</coordinates>', '')
                    line = line.replace('\t', '')
                    line = line.replace('\n', '')
                    coordinates_list.append(line.split(','))
            input_file.close()
            i = 0
            print(len(coordinates_list))
            if(len(coordinates_list) > 0):
                while(i < len(coordinates_list)):
                    pdb.set_trace()
                    waypoint = Waypoint(coordinates_list[i], coordinates_list[i+1], coordinates_list[i+2])
                    waypoints.append(waypoint)
                    i += 3
                for waypoint in waypoints:
                    write_file(waypoint)
        return
