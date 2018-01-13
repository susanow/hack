#!/usr/bin/env python3


import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def main():

    fname = "dat_l2fwd1b_delay050_pkt064.dat"
    data = np.loadtxt(fname, delimiter=',')

    input1 = data[:,1]
    input2 = data[:,2]
    input3 = data[:,3]
    input4 = data[:,4]
    plt.plot(input1, label="flow")
    plt.plot(input2, label="test0")
    plt.plot(input3, label="test1")
    plt.plot(input4, label="test2")
    plt.legend(loc=2)
    plt.show()
    plt.savefig("file.png")

    return

if __name__ == '__main__':
    main()

