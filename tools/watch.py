#!/usr/bin/env python3

import sys,ctypes
libc=ctypes.cdll.LoadLibrary('libc.so.6')
popcount=lambda n:libc.__sched_cpucount(
    ctypes.sizeof(ctypes.c_long),(ctypes.c_long*1)(n))

def watch_vnf(vnfname):
    import time
    import susanow
    import math
    nfvi = susanow.nfvi.nfvi()
    vnf = nfvi.get_vnf(vnfname)
    if (vnf == None): exit(-1)

    file = open('/home/slank/tmp.csv', 'w')
    file.write('#{:4}, {:3}, {:3}, {:3}\n'.format(
        'idx', 'rat', 'prf', 'rsc'))

    cnt = 0
    while (True):
        vnf.sync()
        rate = math.floor(vnf.rxrate() / 17500000 * 100)
        perf = math.floor(vnf.perfred() * 100)
        n_cores = popcount(vnf.coremask())
        res = '{:05}, {:03}, {:03}, {:03}\n'.format(
                cnt, rate, perf, math.floor(n_cores/8*100))
        print(res, end='')
        file.write(res)
        file.flush()
        cnt = cnt + 1
        time.sleep(1)

def main():
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    if (argc < 2):
        print("Usage: {} <vnfname>".format(argv[0]))
        exit(-1)
    vnfname = argv[1]
    watch_vnf(vnfname)

if __name__ == '__main__':
    main()

