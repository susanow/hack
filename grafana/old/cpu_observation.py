#!/usr/bin/env python3
#
# MIT License
# Copyright (c) 2017 Susanow
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import math
import time
import sys
from numpy.random import *
from influxdb import InfluxDBClient
import urllib
import urllib.request
import json
import time
import requests

api_root = "http://labnet5.dpdk.ninja:8888"

def get(func):
    try:
        url = api_root + '/' + func
        u = requests.get(url)
        return u.json()
    except:
        d = {}
        d['result'] = {}
        d['result']['success'] = False;
        return d

def main():

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'npstudy')
    client.create_database('npstudy')

    while True:
        res = get('system/cpu')
        if (res['result']['success']):
            json_body = [
                {
                  "measurement" : "demotest",
                  "fields" : {
                  },
                }
            ]
            for i in range(2):
                cpu = res[str(i)]
                for j in range(cpu['n_core']):
                    core = cpu[str(j)]
                    json_body[0]['fields']['lcore' + str(core['lcore_id'])] =  int(core['usage_rate'])

            print(res['n_cpu'])
            for k in range(res['n_cpu']):
                cpu = res[str(k)]
                for kk in range(cpu['n_core']):
                    core = cpu[str(kk)]
                    core_id = core['lcore_id']
                    usage   = core['usage_rate']
                    print('{:-2}[{:3.0f}%]  '.format(core_id, usage), end='')
                    if ((kk+1) % 4 == 0): print('')
                print('\n')

            client.write_points(json_body)
            time.sleep(1)


if __name__ == '__main__':
    main()

