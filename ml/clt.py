# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt

if __name__=="__main__":
    u = numpy.random.uniform(0.0, 1.0, 10000)
    plt.hist(u, 80, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()
