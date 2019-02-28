import numpy as np
import logging
import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Base(object):
    '''import/outport base class for our algo'''
    def __init__(self, input_file_name):
        self.R, self.C, self.L, self.H = 0, 0, 0, 0

    def read_input(self, input_file_name):
        """ Reading input files """

        with open(os.path.join(project_dir, "input", input_file_name), 'r') as f:
            first_line = f.readline()

            self.R, self.C, self.L, self.H = map(int, first_line.split(' '))
            logging.debug("Input file: Rows %s Columns %s Min %s Max %s", self.R, self.C, self.L, self.H)

            self.pizza = np.zeros((self.R, self.C), dtype=int)

            for i in range(self.R):
                line = f.readline()
                for j in range(self.C):
                    self.pizza[i][j] = (line[j] == "T")

            logging.debug("Pizza:\n %s", self.pizza)

    def write(self, output_file_name):
        """ writing to file """
        with open("output/" + output_file_name, 'w') as f:
            for vehicle in self.result:
                f.write(str(len(vehicle)))
                for ride_id in vehicle:
                    f.write(" " + str(ride_id))
                f.write("\n")