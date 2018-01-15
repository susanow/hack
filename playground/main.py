#!/usr/bin/env python3

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.close()
    plt.ylim([0,105])
    plt.ylabel('Rate [%]')
    plt.xlabel('Time [sec]')
    plt.title('Auto Optimization of Traffic Process using D2')

    tmp = pd.read_csv('tmp.csv',
            names=['flow', 'd2opt', 'resrc'],
            comment='#')
    ct1 = pd.read_csv('1thrd_dat.csv', names=['flow', 'tpr'], comment='#')
    ct4 = pd.read_csv('4thrd_dat.csv', names=['flow', 'tpr'], comment='#')

    plt.plot(tmp['flow'], label="10GbE Traffic pktsize=128Byte flexrate")
    plt.plot(tmp['d2opt'], label="Traffic Process Rate using d2-auto-optimization")
    # plt.plot(ct1['tpr'], label="# of thread = 1 const")
    # plt.plot(ct4['tpr'], label="# of thread = 4 const")
    plt.plot(tmp['resrc'], label="Computer resource for PktFwd")
    plt.legend(loc=4, fontsize=8)
    plt.savefig('out.png')


if __name__ == '__main__':
    main()

