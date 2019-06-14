# Write the benchmarking functions here.
# See "Writing benchmarks" in the asv docs for more information.


import numba as nb
import numpy as np


class TimeSuite:
    """
    An example benchmark that times the performance of various kinds
    of iterating over dictionaries in Python.
    """
    def setup(self):
        self.d = {}
        for x in range(500):
            self.d[x] = None

    def time_keys(self):
        for key in self.d.keys():
            pass

    def time_iterkeys(self):
        for key in self.d.iterkeys():
            pass

    def time_range(self):
        d = self.d
        for key in range(500):
            x = d[key]

    def time_xrange(self):
        data = np.random.rand(100_000)
        x = az.bfmi(data)
        return x


class MemSuite:
    def mem_list(self):
        return [0] * 256
