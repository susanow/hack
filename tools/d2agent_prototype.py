#!/usr/bin/env python3

import sys
import math
import time
import threading
import susanow
import susanow.d2 as d2


def d2out_ignition(vnf, nfvi, threshold):
    perf = vnf.perfred() * 100
    return (perf < threshold)


def d2in_ignition(vnf, nfvi, data):
    perf = vnf.perfred()
    rate = vnf.rxrate()
    p = math.floor((rate * perf) * (rate * perf))

    data_ = data
    diff = 0 if (data[-5]['a']==0) else data[-1]['a'] / data[-5]['a']
    if (diff < 0.7):
        return True
    return False


def d2agent(vnf, nfvi):
    cnt = 0
    while (True):
        cnt = cnt + 1
        vnf.sync()
        n_core = vnf.n_core()
        rxrate = vnf.rxrate()
        perf = math.floor(vnf.perfred() * 100)
        perf = 100 if (perf>100) else perf
        print('{:03}% rxrate={}'.format(perf, rxrate))

        max_rate = 17000000

        if (n_core == 1):

            if (perf < 90):
                print('out')
                d2.d2out(vnf, nfvi)

        elif (n_core == 2):

            if (perf < 90):
                print('out')
                d2.d2out(vnf, nfvi)

            if (perf > 85):
                if (rxrate < (max_rate*0.3)):
                    print('in2')
                    d2.d2in(vnf, nfvi)

        elif (n_core == 4):

            if (perf > 85):
                if (rxrate < (max_rate*0.6)):
                    print('in1')
                    d2.d2in(vnf, nfvi)

        time.sleep(0.5)



def main():
    argc = len(sys.argv)
    argv = sys.argv
    if (argc < 2):
        print("Usage: {} <vnfname>".format(argv[0]))
        exit(-1)

    nfvi = susanow.nfvi.nfvi()
    vnf = nfvi.get_vnf(argv[1])
    if (vnf == None):
        print('vnf not found')
        exit(-1)

    d2agent(vnf, nfvi)


if __name__ == '__main__':
    main()

