#!/usr/bin/env python3

import urllib
import urllib.request
import json
import time
import requests
import math
import susanow
import sys,ctypes

libc=ctypes.cdll.LoadLibrary('libc.so.6')
popcount=lambda n:libc.__sched_cpucount(
    ctypes.sizeof(ctypes.c_long),(ctypes.c_long*1)(n))

nfvi = susanow.nfvi.nfvi('labnet5.dpdk.ninja')
vnf0 = nfvi.get_vnf('vnf0')
api_root = "http://labnet5.dpdk.ninja:8888"

def get(func):
    url = api_root + '/' + func
    u = requests.get(url)
    return u.json()

f = open('/home/slank/tmp.csv', 'w')
s = '#idx , flow , proc , resrc\n'
f.write(s)
print(s, end='')
idx = 0
while True:
    vnf0.sync()
    n_core = popcount(vnf0.coremask())
    res = get('system/pnic')
    n_pnic = res['n_pnic']
    sum_rx_pkts = 0
    sum_rate    = 0
    for i in range(n_pnic):
        pnic = res[str(i)]
        proc = int(pnic['cur_rx_pps'])
        rx_pkts = int(pnic['cur_rx_pps'] + pnic['cur_rx_mis'])
        rate = 0 if rx_pkts == 0 else math.floor(proc / rx_pkts * 100)
        sum_rx_pkts = sum_rx_pkts + rx_pkts
        sum_rate = sum_rate + rate
    s = '{:05}, {:05}, {:05}, {:05}\n'.format(
        idx,
        math.floor(sum_rx_pkts / (2*8500000) * 100),
        math.floor(sum_rate/2),
        math.floor(n_core / 4 * 100))
    print(s, end='')
    f.write(s)
    f.flush()
    idx = idx + 1
    time.sleep(1)


