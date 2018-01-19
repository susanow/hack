#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint


def main():

    data = np.loadtxt('/tmp/ssn_record.csv', delimiter=',', comments='#')
    idx      = data[:,0]
    ts       = data[:,1]
    vnf0traf = data[:,2]
    vnf0tpr  = data[:,3]
    vnf0core = data[:,4]
    vnf1traf = data[:,5]
    vnf1tpr  = data[:,6]
    vnf1core = data[:,7]

    xbegin = 0
    xend   = 1100

    fig, ax1 = plt.subplots(2)
    ax1[1].set_xlabel('time [sec]')

    ax1[0].set_ylabel('Traffic Process Rate [%]')
    ax1[0].set_ylim([0,120])
    ax1[0].set_xlim([xbegin, xend])
    ax1[0].plot(idx, vnf0tpr, color="b")
    ax1[0].plot(idx, vnf1tpr, color="r")

    ax2 = ax1[0].twinx()
    ax2.set_ylabel('Traffic Rate [pps]')
    ax2.set_xlim([xbegin, xend])
    ax2.set_ylim([0, 25000000])
    ax2.bar(idx, vnf0traf, color="b")
    ax2.bar(idx, vnf1traf, bottom=vnf0traf,color="r")

    ax1[1].set_ylabel('Traffic Process Rate [%]')
    ax1[1].set_ylim([0,120])
    ax1[1].set_xlim([xbegin, xend])
    ax1[1].plot(idx, vnf0tpr, color="b")
    ax1[1].plot(idx, vnf1tpr, color="r")

    ax2 = ax1[1].twinx()
    ax2.set_ylabel('Conputer Resourcing [#cores]')
    ax2.set_xlim([xbegin, xend])
    ax2.set_ylim([0, 10])
    ax2.bar(idx, vnf0core, color="b")
    ax2.bar(idx, vnf1core, bottom=vnf0core, color="r")

    # ax1.legend(loc=0, fontsize=8)
    # ax2.legend(loc=4, fontsize=8)
    plt.savefig('out.png')


if __name__ == '__main__':
    main()

