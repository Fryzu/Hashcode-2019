from .base import Base
import numpy as np
import tqdm
import logging

class Solver(Base):
    def solve(self):
        '''creating two groups'''


        for i in self.photos_list:
            if i[1]:
                self.verticals.append(i)
            else:
                self.horizontals.append(i)



        logging.debug("Horizontals: %s", len(self.horizontals))
        logging.debug("Verticals: %s", len(self.verticals))

        # making one slide from 2 vertical pictures
        ll = int(len(self.horizontals)/2)
        l = ll
        pbar = tqdm.tqdm(total=ll, desc='Computing time')
        for _ in range(l):

            c1 = np.random.randint(0, ll)
            ll-=1
            c2 = np.random.randint(0, ll)
            while c1 == c2:
                c2 = np.random.randint(0, len(self.horizontals))
            #self.horizontals_slides.append((self.horizontals[c1], self.horizontals[c2]))
            #print(c1, c2)
            self.verticals.append((self.horizontals[c1], self.horizontals[c2]))
            pbar.update(1)
            ll-=1

        self.result = self.verticals

        #logging.debug("Result: %s", self.verticals)
        pbar.close()

        return True

