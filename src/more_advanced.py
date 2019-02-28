from .base import Base
import numpy as np
import tqdm
import logging
from itertools import combinations

class Solver(Base):
    def merge(self, toMerge):
        return (-1, True, list(set(toMerge[0][2]+toMerge[1][2])))

    def solve(self):
        '''creating two groups'''
        self.horizontals = []
        self.verticals = []

        for i in self.photos_list:
            if i[1]:
                self.verticals.append(i)
            else:
                self.horizontals.append(i)

        self.verticals_pairs = list(combinations(self.verticals, 2)) 
        logging.debug("Horizontals: %s", self.horizontals)
        logging.debug("Vertical pairs: %s", self.verticals_pairs)
        logging.debug("Vertical pairs merged: %s", self.merge(self.verticals_pairs[0]))
        self.value((-1, True, ["a","b"]), (-1, True, ["b","c"]))



        ''' Algo starts ''' 
        self.result.append(self.horizontals[0])
        del self.horizontals[0]
        while True:
            ''' Finding best neighbour '''
            best_neighbour = None
            break

        return True