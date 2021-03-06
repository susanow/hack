#!/usr/bin/env python3

import math, sys
import numpy as np
# import matplotlib
# matplotlib
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from pprint import pprint

def get_avg(array):
    sumd = 0;
    for i in array:
        sumd = sumd + i
    return math.floor(sumd/len(array))

def main():

    d2di_filename = "d2disable55fix_d100.csv"
    d2en_filename = "d2enable_d100.csv"
    outfilename = "out.png"

    print("d2disable file : {}".format(d2di_filename))
    print("d2enable  file : {}".format(d2en_filename))
    print("output    file : {}".format(outfilename))

    di_data = np.loadtxt(d2di_filename, delimiter=',', comments='#')
    di_idx      = di_data[:,0]
    di_ts       = di_data[:,1]
    di_vnf0traf = di_data[:,2]
    di_vnf0tpr  = di_data[:,3]
    di_vnf0core = di_data[:,4]
    di_vnf1traf = di_data[:,5]
    di_vnf1tpr  = di_data[:,6]
    di_vnf1core = di_data[:,7]

    en_data = np.loadtxt(d2en_filename, delimiter=',', comments='#')
    en_idx      = en_data[:,0]
    en_ts       = en_data[:,1]
    en_vnf0traf = en_data[:,2]
    en_vnf0tpr  = en_data[:,3]
    en_vnf0core = en_data[:,4]
    en_vnf1traf = en_data[:,5]
    en_vnf1tpr  = en_data[:,6]
    en_vnf1core = en_data[:,7]

    xbegin = 0
    xend   = 200
    bar_width = 1.0
    vnf0_color = "red"
    vnf1_color = "blue"

    fig, ax1 = plt.subplots(3)
    ax1[2].set_xlabel('time [sec]')

    ax1[0].set_ylabel('Traffic [pps]')
    ax1[0].set_ylim([0, 25000000])
    ax1[0].set_xlim([xbegin, xend])
    ax1[0].bar(di_idx, di_vnf0traf,
            width=bar_width,
            edgecolor="none",
            color=vnf0_color,
            label='vnf0')
    ax1[0].bar(di_idx, di_vnf1traf,
            width=bar_width,
            edgecolor="none",
            bottom=di_vnf0traf,
            color=vnf1_color,
            label='vnf1')
    ax1[0].legend(loc=1, fontsize=8)

    ax1[1].set_ylabel('D2disable\n#Cores')
    ax1[1].set_xlim([xbegin, xend])
    ax1[1].set_ylim([0, 22])
    ax1[1].bar(di_idx, di_vnf0core,
            width=bar_width,
            edgecolor="none",
            color=vnf0_color,
            label='vnf0')
    ax1[1].bar(di_idx, di_vnf1core,
            width=bar_width,
            edgecolor="none",
            bottom=di_vnf0core,
            color=vnf1_color,
            label='vnf1')
    ax1[1].legend(loc=1, fontsize=8)

    ax2 = ax1[1].twinx()
    ax2.set_ylabel('Process Rate [%]')
    ax2.set_ylim([0,110])
    ax2.set_xlim([xbegin, xend])
    ax2.plot(di_idx, di_vnf0tpr,
            color=vnf0_color,
            label= 'vnf0 avg={}'.format(get_avg(di_vnf0tpr)))
    ax2.plot(di_idx, di_vnf1tpr,
            color=vnf1_color,
            label='vnf1 avg={}'.format(get_avg(di_vnf1tpr)))
    ax2.legend(loc=1, fontsize=8)

    ax1[2].set_ylabel('D2enable\n#Cores')
    ax1[2].set_xlim([xbegin, xend])
    ax1[2].set_ylim([0, 22])
    ax1[2].bar(en_idx, en_vnf0core,
            width=bar_width,
            edgecolor="none",
            color=vnf0_color,
            label='vnf0')
    ax1[2].bar(en_idx, en_vnf1core,
            width=bar_width,
            edgecolor="none",
            bottom=en_vnf0core,
            color=vnf1_color,
            label='vnf1')
    ax1[2].legend(loc=1, fontsize=8)

    ax2 = ax1[2].twinx()
    ax2.set_ylabel('Process Rate [%]')
    ax2.set_ylim([0,110])
    ax2.set_xlim([xbegin, xend])
    ax2.plot(en_idx, en_vnf0tpr,
            color=vnf0_color,
            label= 'vnf0 avg={}'.format(get_avg(en_vnf0tpr)))
    ax2.plot(en_idx, en_vnf1tpr,
            color=vnf1_color,
            label='vnf1 avg={}'.format(get_avg(en_vnf1tpr)))
    ax2.legend(loc=1, fontsize=8)

    plt.savefig(outfilename, dpi=150)


if __name__ == '__main__':
    main()







