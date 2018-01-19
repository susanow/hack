#!/usr/bin/env python3

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt



def main():
    # plt.ylim([0,105])
    # plt.ylabel('Rate [%]')
    # plt.xlabel('Time [sec]')
    # plt.title('Totemo Totemo SUGOI NFV')

    vnf0 = pd.read_csv('/tmp/ssn_vnf0_perfmonitor.csv',
            names=['flow', 'tpr', 'ncore'], comment='#')
    vnf1 = pd.read_csv('/tmp/ssn_vnf1_perfmonitor.csv',
            names=['flow', 'tpr', 'ncore'], comment='#')


    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax2.set_ylim([0,200])

    ax1.plot(vnf0['flow'], color="r", label="vnf0-trafiic")
    ax1.plot(vnf1['flow'], color="b", label="vnf1-traffic")
    ax2.plot(vnf0['tpr'], label="vnf0 TPR", )
    ax2.plot(vnf1['tpr'], label="vnf1 TPR")
    ax1.legend(loc=0, fontsize=8)
    ax2.legend(loc=4, fontsize=8)
    # plt.xlim([1516327378, 1516427448])
    fig.savefig('out.png')


if __name__ == '__main__':
    main()

