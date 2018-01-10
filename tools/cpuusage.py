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
    # print('cnt={}'.format(count))
    res = get('system/cpu')
    if (res['result']['success'] != True):
        print('Unsuccess Error')
        exit(-1)

    n_cpu = res['n_cpu']
    for i in range(n_cpu):
        cpu = res[str(i)]
        n_core = cpu['n_core']
        # print(cpu['n_core'])
        print('socket{}'.format(i))
        for j in range(n_core):
            core_id = cpu[str(j)]['lcore_id']
            usage = cpu[str(j)]['usage_rate']
            print('{:-2}[{:3.0f}%]  '.format(core_id, usage), end='')
            if ((j+1) % 4 == 0): print('')
        print('\n')
    print('----------------')
    time.sleep(1)


