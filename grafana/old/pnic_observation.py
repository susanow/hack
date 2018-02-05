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
    url = api_root + '/' + func
    u = requests.get(url)
    return u.json()

def main():

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'npstudy')
    client.create_database('npstudy')

    while True:
        res = get('system/pnic')
        n_pnic = res['n_pnic']
        pnic0 = res['0']
        pnic1 = res['2']
        rx_rate0 = int(pnic0['cur_rx_pps'] + pnic0['cur_rx_mis'])
        rx_rate1 = int(pnic1['cur_rx_pps'] + pnic1['cur_rx_mis'])
        print('port0: {}bps'.format(rx_rate0))
        print('port1: {}bps'.format(rx_rate1))
        json_body = [
            {
              "measurement" : "demotest",
              "fields" : {
                "rx_rates0" : rx_rate0,
                "rx_rates1" : rx_rate1,
              },
            }
        ]
        print(json_body)
        client.write_points(json_body)
        time.sleep(1)


if __name__ == '__main__':
    main()

