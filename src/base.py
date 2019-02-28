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

            logging.debug(self.photos_list)

    def write(self, output_file_name):
        """ writing to file """
        with open("output/" + output_file_name, 'w') as f:
            f.write(str(len(self.result)))
            f.write("\n")
            for picture in self.result:
                if len(picture)>1:
                    f.write(str(picture[0]))
                    f.wtite(" ")
                    f.write(str(picture[1]))
                    f.write("\n")

    def value(self, first, second):
        '''Calculets points for S and S+1'''
        
        setFirst = set(first[2])
        setSecond = set(second[2])

        #logging.debug("Cacluating value of two: %s %s", setFirst, setSecond)

        intersection = setFirst.intersection(setSecond)
        onlyInFirst = setFirst - intersection
        onlyInSecond = setSecond - intersection

        
        #logging.debug("Intersection %s", intersection)
        #logging.debug("OnlyInFirst %s", onlyInFirst)
        #logging.debug("OnlyInSecond %s", onlyInSecond)

        result = min(len(intersection), len(onlyInFirst), len(onlyInSecond))
        #logging.debug("Points earned %s", result)

        return result