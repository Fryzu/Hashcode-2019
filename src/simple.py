from .base import Base
import numpy as np
import tqdm
import logging

class Solver(Base):
    def solve(self):
        self.photos_list_copy = self.photo_list
        self.photos_list_horizontal = []
        for photo in range(self.N):
            if self.photos_list[photo][1] == True:
                self.photos_list_horizontal.append(self.photos_list[photo])

            choice = np.random.randint(1,self.N)
            self.result.append(self.photos_list_copy[choice])
            self.photos_list_copy.remove(self.photos_list_copy[choice])

        return True
