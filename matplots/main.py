#!/usr/bin/env python3

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def main():

    plt.plot( [1,2,3], 'b') # 青
    plt.plot( [1,2,3], 'g') # 緑
    plt.plot( [1,2,3], 'r') # 赤
    plt.plot( [1,2,3], 'c') # シアン
    plt.plot( [1,2,3], 'm') # マゼンタ
    plt.plot( [1,2,3], 'y') # イエロー
    plt.plot( [1,2,3], 'b') # 黒
    plt.plot( [1,2,3], 'w') # 白

    # # プロット方式と同時指定
    plt.plot( [1,2,3], '--b') # 破線 + 青
    plt.savefig("file.png")

    return

if __name__ == '__main__':
    main()

