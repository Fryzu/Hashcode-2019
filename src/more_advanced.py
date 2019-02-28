from .base import Base
import numpy as np
import tqdm
import logging
from itertools import combinations

class Solver(Base):
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

        return True