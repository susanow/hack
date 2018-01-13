#!/usr/bin/env python3

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.close()
    plt.ylim([0,105])
    inputname  = 'tmp.csv'
    outputname = 'out.png'

    data = pd.read_csv(inputname, names=['flow', '1thrd', '4thrd'], comment='#')
    plt.plot(data['flow'], label="Traffic pktsize=128Byte")
    plt.plot(data['1thrd'], label="TPR 1thrd-const")
    plt.plot(data['4thrd'], label="TPR 4thrd-const")
    plt.legend(loc=4, fontsize=8)
    plt.savefig(outputname)


if __name__ == '__main__':
    main()

