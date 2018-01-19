#!/usr/bin/env python3

import math
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pprint import pprint



def main():
    # plt.ylim([0,105])
    # plt.ylabel('Rate [%]')
    # plt.xlabel('Time [sec]')
    # plt.title('Totemo Totemo SUGOI NFV')

    vnf0 = pd.read_csv('ssn_vnf0_perfmonitor.csv',
            names=['ts', 'flow', 'tpr', 'ncore'], comment='#')
    vnf1 = pd.read_csv('ssn_vnf1_perfmonitor.csv',
            names=['ts', 'flow', 'tpr', 'ncore'], comment='#')

    for i in range(len(vnf0["ncore"])):
        tmp = vnf0["ncore"][i+1]
        vnf0["ncore"][i] = math.floor(tmp / 4.0 * 100)

    for i in range(len(vnf1["ncore"])):
        tmp = vnf1["ncore"][i+1]
        vnf1["ncore"][i] = math.floor(tmp / 4.0 * 100)

    fig, ax1 = plt.subplots()
    ax1.plot(vnf0['flow'], color='b', label="vnf0 traffic", linestyle="dotted")
    ax1.plot(vnf1['flow'], color='r', label="vnf1 traffic", linestyle="dotted")

    ax2 = ax1.twinx()
    ax2.plot(vnf0['tpr'], color="b", label="vnf0 TPR", linestyle="solid")
    ax2.plot(vnf1['tpr'], color="r", label="vnf1 TPR", linestyle="solid")
    ax2.plot(vnf0['ncore'], color="b", label="vnf0 cores", linestyle="dashed")
    ax2.plot(vnf1['ncore'], color="r", label="vnf1 cores", linestyle="dashed")

    ax1.legend(loc=0, fontsize=8)
    ax2.legend(loc=4, fontsize=8)
    ax1.set_ylim([0, 20000000])
    ax2.set_ylim([0, 120])
    plt.savefig('out.png')


if __name__ == '__main__':
    main()

