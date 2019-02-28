import numpy as np
import logging
import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Base(object):
    '''import/outport base class for our algo'''
    def __init__(self, input_file_name):
        self.N = 0
        self.photos_list = []
        self.result = []

    def read_input(self, input_file_name):
        """ Reading input files """

        with open(os.path.join(project_dir, "input", input_file_name), 'r') as f:
            first_line = f.readline()

            self.N = int(first_line.rstrip())
            logging.debug("Number of photos %s", self.N)

            for i in range(self.N):
                line = f.readline().replace('\n', '')
                line_argument_list = line.split(' ')
                verticalOrHorizontal = (line_argument_list[0] == "V")
                tagsCount = int(line_argument_list[1])
                tagsList = []
                for j in range(tagsCount):
                    tagsList.append(line_argument_list[j+2])
                self.photos_list.append((i, verticalOrHorizontal, tagsList))

            #logging.debug(self.photos_list)

    def write(self, output_file_name):
        """ writing to file """
        with open("output/" + output_file_name, 'w') as f:
            for vehicle in self.result:
                f.write(str(len(vehicle)))
                for ride_id in vehicle:
                    f.write(" " + str(ride_id))
                f.write("\n")
