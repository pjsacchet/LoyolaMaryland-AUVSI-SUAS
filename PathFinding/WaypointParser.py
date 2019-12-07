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
        self.output_filename = "Logs/" + dt_str + ".txt"
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

    # Format a line taken from .kml file for waypoint object creation
    # Input: line - line to be formatted
    # Returns: line - newly formatted line
    def format_line(self, line):
        line = line.replace('<coordinates>', '')
        line = line.replace('</coordinates>', '')
        line = line.replace('\t', '')
        line = line.replace('\n', '')
        lien = line.replace(' ', ',')
        return line

    def format_newline(self, line):
        # While the next line does not contain 'airDropPos'...
        while(line.next)
            # Check for the fields for specfiic parameters 
        line = line.replace()
        return line

    # Parses the file passed to create waypoint objects
    # Input: None
    # Returns: None
    def parse_file(self):
        # Parse through file until reaching '<Waypoints>' tag in .kml
        # Check that file actually exists, if not print error and return
        if(os.path.exists(self.file_loc) == False):
            print("File location doesn't exist bud, try again \n")
            return
        # Else, file actually exists so lets get started
        else:
            # Initialize list of waypoint objects and the list for the actual coordinates
            waypoints = []
            coordinates_list = []
            # Open the file and begin to iterate over data, with each waypoint created, write to the output file
            input_file = open(self.file_loc, "r")
            line = input_file.readline()
            while(line):
            # For each line in the file...
                # If the line contains the coordinates tag...
                if("waypoints" in line):
                    # Get rid of the start and end tags, then set delimiters and create waypoint objects
                    line = self.format_line(line)
                    # If the line isnt blank after parsing go ahead and split it and add the coordinates
                    if(line.split(',') != ['']):
                        coordinates_list.append(line.split(','))
                    # Else, this line has nothing in it, meaning the coordinates are actually on the next line
                    else:
                        line = input_file.readline()
                        line = self.format_line(line)
                        print(line.split(','))
                        coordinates_list.append(line.split(','))
                        # Want to go to next line since it is just the closing brackets for coordinate
                        line = input_file.readline()
                line = input_file.readline()
            input_file.close()
            i = 0
            # Assuming we found coordinates within the .kml file...
            if(len(coordinates_list) > 0):
                while(i < len(coordinates_list)):
                    # Create a waypoint object with its x y and z components to be added to our waypointsdd list
                    waypoint = Waypoint(coordinates_list[i][0], coordinates_list[i][1], coordinates_list[i][2])
                    waypoints.append(waypoint)
                    i += 1
                for waypoint in waypoints:
                    self.write_file(str(waypoint))
        return
