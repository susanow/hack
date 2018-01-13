#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def l2fwd1b_delay000_pkt064():
    inputname  = 'dat_l2fwd1b_delay000_pkt064.dat'
    outputname = 'delay000_pkt064'
    print('{}(in={}, out={})'.format(
        sys._getframe().f_code.co_name,
        inputname, outputname))

    data = np.loadtxt(inputname, delimiter=',')
    input1 = data[:,1]
    input2 = data[:,2]
    input3 = data[:,3]
    input4 = data[:,4]
    plt.plot(input1, label="Traffic pktsize=64Byte")
    plt.plot(input2, label="TPR #thrd=1, delay=0")
    plt.plot(input3, label="TPR #thrd=2, delay=0")
    plt.plot(input4, label="TPR #thrd=4, delay=0")
    plt.legend(loc=2)
    plt.savefig(outputname)

def l2fwd1b_delay050_pkt064():
    inputname  = 'dat_l2fwd1b_delay050_pkt064.dat'
    outputname = 'delay050_pkt064'
    print('{}(in={}, out={})'.format(
        sys._getframe().f_code.co_name,
        inputname, outputname))

    data = np.loadtxt(inputname, delimiter=',')
    input1 = data[:,1]
    input2 = data[:,2]
    input3 = data[:,3]
    input4 = data[:,4]
    plt.plot(input1, label="Traffic pktsize=64Byte")
    plt.plot(input2, label="TPR #thrd=1, delay=50")
    plt.plot(input3, label="TPR #thrd=2, delay=50")
    plt.plot(input4, label="TPR #thrd=4, delay=50")
    plt.legend(loc=2)
    plt.savefig(outputname)

def l2fwd1b_delay050_pkt128():
    inputname  = 'dat_l2fwd1b_delay050_pkt128.dat'
    outputname = 'delay050_pkt128'
    print('{}(in={}, out={})'.format(
        sys._getframe().f_code.co_name,
        inputname, outputname))

    data = np.loadtxt(inputname, delimiter=',')
    input1 = data[:,1]
    input2 = data[:,2]
    input3 = data[:,3]
    input4 = data[:,4]
    plt.plot(input1, label="Traffic pktsize=128Byte")
    plt.plot(input2, label="TPR #thrd=1, delay=50")
    plt.plot(input3, label="TPR #thrd=2, delay=50")
    plt.plot(input4, label="TPR #thrd=4, delay=50")
    plt.legend(loc=2)
    plt.savefig(outputname)

def l2fwd1b_delay100_pkt064():
    inputname  = 'dat_l2fwd1b_delay100_pkt064.dat'
    outputname = 'delay100_pkt064'
    print('{}(in={}, out={})'.format(
        sys._getframe().f_code.co_name,
        inputname, outputname))

    data = np.loadtxt(inputname, delimiter=',')
    input1 = data[:,1]
    input2 = data[:,2]
    input3 = data[:,3]
    input4 = data[:,4]
    plt.plot(input1, label="Traffic pktsize=64Byte")
    plt.plot(input2, label="TPR #thrd=1, delay=100")
    plt.plot(input3, label="TPR #thrd=2, delay=100")
    plt.plot(input4, label="TPR #thrd=4, delay=100")
    plt.legend(loc=2)
    plt.savefig(outputname)

def main():
    plt.close()
    plt.ylim([0,105])
    l2fwd1b_delay000_pkt064()

    plt.close()
    plt.ylim([0,105])
    l2fwd1b_delay050_pkt064()

    plt.close()
    plt.ylim([0,105])
    l2fwd1b_delay050_pkt128()

    plt.close()
    plt.ylim([0,105])
    l2fwd1b_delay100_pkt064()

if __name__ == '__main__':
    main()

