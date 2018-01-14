#!/usr/bin/env python3

import urllib
import urllib.request
import json
import time
import requests
import math

api_root = "http://labnet5.dpdk.ninja:8888"

def get(func):
    url = api_root + '/' + func
    u = requests.get(url)
    return u.json()

f = open('/home/slank/tmp.csv', 'w')
idx = 0
while True:
    res = get('system/pnic')
    n_pnic = res['n_pnic']
    sum_rx = 0
    for i in range(n_pnic):
        pnic = res[str(i)]
        rx_pkts = int(pnic['cur_rx_pps'] + pnic['cur_rx_mis'])
        sum_rx = sum_rx + rx_pkts
        print('port{}: {}bps'.format(i, rx_pkts))
    print('--------------')
    f.write('{}, {}\n'.format(idx, math.floor(sum_rx/(2*8500000) * 100) ))
    f.flush()
    time.sleep(1)
    idx = idx + 1


