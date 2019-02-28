from .base import Base
import numpy as np
import tqdm
import logging

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

        logging.debug("Horizontals: %s", self.horizontals)
        logging.debug("Verticals: %s", self.verticals)

        return True