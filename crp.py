"""
The Chinese Restaurant Process

Consider a restaurant with an infinite number of tables 
and an infinite number of seats at each table.
A sequence of N customers arrive labeled {1, ..., N}
The first customer sits at the first table;
the nth subsequence customer sits at a table drawn from the following distribution

theta: discount parameter
gamma: concentration parameter

p(occupied table i | previous customers) = |b| - gamma / theta + i - 1
p(next unoccupied table | previous customers) = theta + |B|*gamma / theta + i - 1


TODO:
    1. is there a reduction to the MST problem (the edge on a cut must be in the mst)
    For multiple parallel distributions of crp is there a 1 inversion net increase
    maybe for optimizing clustering


    2. Generalize CRP 
"""

from collections import defaultdict
import numpy as np

class CRP:

    def __init__(self, theta, gamma):
        self.theta = theta
        self.gamma = gamma
        #each table is an element in an ith indexed array
        self.tables = []
    
        # counts how many customers have arrived
        self._i = 0
        # counts how many tables there are
        self._B = 0

    def draw(self):
        if self._i == 0:
            # base case: no one is seated
            self.new_table()
        else:
            choice = np.random.choice(range(self._B + 1), p=self.dist)
            if choice == self._B:
                self.new_table()
            else:
                self.tables[choice] += 1
        self._i += 1

    def new_table(self):
        # add first customer to first table
        self.tables.append(1)
        # increment number of tables
        self._B += 1

    @property
    def dist(self):
        dist = [bi - self.gamma for bi in self.tables] \
        + [self.theta + self._B * self.gamma]
        dist = [pi / (self.theta + self._i) for pi in dist]
        return dist

    def __repr__(self):
        return f"i {self._i} B {self._B} tables {self.tables} dist {self.dist}"

theta = .5
crp = CRP(theta, 0)
N = 100000
for _ in range(N):
    crp.draw()
print(crp.tables)
