from .base import Base
import numpy as np
import tqdm
import logging

class Solver(Base):
    def solve(self):
        #self.photos_list_copy = self.photos_list
        self.photos_list_horizontal = []
        self.photos_list_vertical = self.photos_list

        for photo in range(self.N):
            if self.photos_list[photo][1] == False:
                self.photos_list_horizontal.append(self.photos_list[photo])
                self.photos_list_vertical.remove(self.photos_list[photo])

        for photo in range(self.N):
            choice = np.random.randint(1,self.N)
            self.result.append(self.photos_list_copy[choice])
            self.photos_list_copy.remove(self.photos_list_copy[choice])

        return True

