#!/usr/bin/env python3

import math, sys
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from pprint import pprint

def get_avg(array):
    sumd = 0;
    for i in array:
        sumd = sumd + i
    return math.floor(sumd/len(array))

def main():

    infilename  = "/tmp/ssn_record.csv"
    outfilename = "out.png"
    if (len(sys.argv) > 2):
        infilename  = sys.argv[1]
        outfilename = sys.argv[2]

    print("input : {}".format(infilename))
    print("output: {}".format(outfilename))

    data = np.loadtxt(infilename, delimiter=',', comments='#')
    idx      = data[:,0]
    ts       = data[:,1]
    vnf0traf = data[:,2]
    vnf0tpr  = data[:,3]
    vnf0core = data[:,4]
    vnf1traf = data[:,5]
    vnf1tpr  = data[:,6]
    vnf1core = data[:,7]

    avg_tpr = []
    for i in range(len(vnf1tpr)):
        avg = (vnf1tpr[i] + vnf0tpr[i])/2
        avg = math.floor(avg)
        avg_tpr.append(avg)

    xbegin = 0
    xend   = 170  # 1times
    xend   = 1100 # 8times
    xend   = 600  # 4times
    xend   = 220  # kukei

    fig, ax1 = plt.subplots(3)
    ax1[2].set_xlabel('time [sec]')

    ax1[0].set_ylabel('Traffic [pps]')
    ax1[0].set_ylim([0, 25000000])
    ax1[0].set_xlim([xbegin, xend])
    ax1[0].bar(idx, vnf0traf, color="r", label='vnf0')
    ax1[0].bar(idx, vnf1traf, bottom=vnf0traf,color="b", label='vnf1')
    ax1[0].legend(loc=1, fontsize=8)

    ax1[1].set_ylabel('[#cores]')
    ax1[1].set_xlim([xbegin, xend])
    ax1[1].set_ylim([0, 20])
    ax1[1].bar(idx, vnf0core, color="r", label='vnf0')
    ax1[1].bar(idx, vnf1core, bottom=vnf0core, color="b", label='vnf1')
    ax1[1].legend(loc=1, fontsize=8)

    ax1[2].set_ylabel('Process Rate [%]')
    ax1[2].set_ylim([0,120])
    ax1[2].set_xlim([xbegin, xend])
    labelstr = 'vnf0 avg={}'.format(get_avg(vnf0tpr))
    ax1[2].plot(idx, vnf0tpr, color="r", label=labelstr)
    labelstr = 'vnf1 avg={}'.format(get_avg(vnf1tpr))
    ax1[2].plot(idx, vnf1tpr, color="b", label=labelstr)
    labelstr = 'all avg={}'.format(get_avg(avg_tpr))
    ax1[2].plot(idx, avg_tpr, color="g", label=labelstr)
    ax1[2].legend(loc=1, fontsize=8)

    plt.savefig(outfilename, dpi=150)


if __name__ == '__main__':
    main()

