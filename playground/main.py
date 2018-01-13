#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.close()
    plt.ylim([0,105])
    inputname  = 'tmp.dat'
    outputname = 'out.png'
    print('{}(in={}, out={})'.format(
        sys._getframe().f_code.co_name,
        inputname, outputname))

    data = np.loadtxt(inputname, delimiter=',')
    input1 = data[:,1]
    input2 = data[:,2]
    input3 = data[:,3]
    input4 = data[:,4]
    input5 = data[:,5]
    plt.plot(input1, label="Traffic pktsize=64Byte")
    plt.plot(input2, label="TPR delay=0 #thread=4")
    plt.plot(input3, label="TPR delay=20 #thread=4")
    plt.plot(input4, label="TPR delay=50 #thread=4")
    plt.plot(input5, label="TPR delay=100 #thread=4")
    plt.legend(loc=2)
    plt.savefig(outputname)


if __name__ == '__main__':
    main()

