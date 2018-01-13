#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def draw_fig(delay, pktsize, f_idx, t1_idx, t2_idx, t4_idx):
    inputname  = 'sinewave_traffic.csv'
    outputname = 'delay{:03}_pkt{:03}'.format(delay, pktsize)
    print('{}(in={}, out={})'.format(
        sys._getframe().f_code.co_name,
        inputname, outputname))

    data = np.loadtxt(inputname, delimiter=',')
    flow  = data[:,f_idx]
    thrd1 = data[:,t1_idx]
    thrd2 = data[:,t2_idx]
    thrd4 = data[:,t4_idx]

    plt.ylim([0,105])
    plt.plot(flow, label="Traffic pktsize={}Byte".format(pktsize))
    plt.plot(thrd1, label="TPR #thrd=1, delay={}".format(delay))
    plt.plot(thrd2, label="TPR #thrd=2, delay={}".format(delay))
    plt.plot(thrd4, label="TPR #thrd=4, delay={}".format(delay))
    plt.legend(loc=2)
    plt.savefig(outputname)
    plt.close()


def main():
    draw_fig(delay=0  , pktsize=64 , f_idx=1, t1_idx=2 , t2_idx=3 , t4_idx=4 )
    draw_fig(delay=0  , pktsize=128, f_idx=1, t1_idx=5 , t2_idx=6 , t4_idx=7 )
    draw_fig(delay=20 , pktsize=64 , f_idx=1, t1_idx=8 , t2_idx=9 , t4_idx=10)
    draw_fig(delay=20 , pktsize=128, f_idx=1, t1_idx=11, t2_idx=12, t4_idx=13)
    draw_fig(delay=50 , pktsize=64 , f_idx=1, t1_idx=14, t2_idx=15, t4_idx=16)
    draw_fig(delay=50 , pktsize=128, f_idx=1, t1_idx=17, t2_idx=18, t4_idx=19)
    draw_fig(delay=100, pktsize=64 , f_idx=1, t1_idx=20, t2_idx=21, t4_idx=22)
    draw_fig(delay=100, pktsize=128, f_idx=1, t1_idx=23, t2_idx=24, t4_idx=25)


if __name__ == '__main__':
    main()

