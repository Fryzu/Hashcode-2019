from .base import Base
import numpy as np
import tqdm
import logging
from itertools import combinations
import random

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

        ''' Algo starts ''' 
        self.result.append(self.horizontals[0])
        del self.horizontals[0]

        pbar = tqdm.tqdm(total=len(self.verticals_pairs)+len(self.horizontals), desc='Computing time')
        while len(self.verticals_pairs) != 0 or len(self.horizontals) != 0:
            '''find best neighbour'''
            pbar.update(1)
            best = -1
            bestNeighbour = None
            bestId = -1

            horizonts = True

            for counter, j in enumerate(self.horizontals):
                tmp = self.value(j, self.result[-1])
                if tmp > best:
                    bestNeighbour = j
                    best = tmp
                    bestId = counter
                    if counter > 100:
                        break

            for counter, j  in enumerate(self.verticals_pairs):
                tmp = self.value(self.merge(j), self.result[-1])
                if tmp > best:
                    bestNeighbour = j
                    best = tmp
                    horizonts = False
                    bestId = counter
                    if counter > 100:
                        break

            ''' deleting becaouse is used'''
            if horizonts:
                self.result.append(self.horizontals[bestId])
                del self.horizontals[bestId]
            else:
                self.result.append(self.verticals_pairs[bestId])
                del self.verticals_pairs[bestId]


        pbar.close()
        print("result %s", self.result)
        
        return True