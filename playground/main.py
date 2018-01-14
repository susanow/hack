#!/usr/bin/env python3

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main():
    plt.close()
    plt.ylim([0,105])
    tmpfile = 'tmp.csv'
    thrd1_file = '1thrd_dat.csv'
    thrd4_file = '4thrd_dat.csv'
    outfile = 'out.png'

    td1 = pd.read_csv(thrd1_file,
            names=['flow', '1thrd', 'resrc'],
            comment='#')

    td4 = pd.read_csv(thrd4_file,
            names=['flow', '4thrd', 'resrc'],
            comment='#')

    tmp = pd.read_csv(tmpfile,
            names=['flow', 'd2opt', 'resrc'],
            comment='#')

    plt.plot(tmp['flow'] , label="Traffic pktsize=128Byte")
    plt.plot(td1['1thrd'], label="TPR 1thrd-const")
    plt.plot(td4['4thrd'], label="TPR 4thrd-const")
    plt.plot(tmp['d2opt'], label="TPR d2 auto optimization")
    plt.plot(tmp['resrc'], label="resourcing")
    plt.legend(loc=4, fontsize=8)
    plt.savefig(outfile)


if __name__ == '__main__':
    main()

