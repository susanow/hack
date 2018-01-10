#!/usr/bin/env python3

import urllib
import urllib.request
import json
import time
import requests

api_root = "http://labnet5.dpdk.ninja:8888"

def get(func):
    url = api_root + '/' + func
    u = requests.get(url)
    return u.json()

while True:
    res = get('system/pnic')
    n_pnic = res['n_pnic']
    for i in range(n_pnic):
        pnic = res[str(i)]
        rx_pkts = int(pnic['cur_rx_pps'] + pnic['cur_rx_mis'])
        print('port{}: {}bps'.format(i, rx_pkts))
    print('--------------')
    time.sleep(1)


