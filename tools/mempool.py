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

count = 0
while True:
    count = count + 1
    print(count)
    res = get('system/mem')
    n_mp = res['n_mempool']
    for i in range(n_mp):
        mp = res[str(i)]
        name  = mp['name']
        size  = mp['size']
        avail = mp['avail']
        r = avail / size
        print('{}: {}/{} [{:.0f}% free]'.format(name, size-avail, size, r*100))
    print('----------------')
    time.sleep(1)


