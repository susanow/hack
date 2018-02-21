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
import susanow

def main():

    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'npstudy')
    client.create_database('npstudy')

    nfvi = susanow.nfvi.nfvi('labnet5.dpdk.ninja', 8888)
    vnf = nfvi.get_vnf('vnf0')
    if (vnf == None):
        print("not found vnf")
        exit(-1)

    while True:
        # vnf.sync()
        # rx_rate = math.floor(vnf.rxrate())
        # vnf_rate = math.floor(vnf.rxrate() * vnf.perfred())
        # vnf_perf = math.floor(vnf.perfred() * 100)


        nfvi.sync()
        vnfs = nfvi.list_vnfs()
        print(vnfs)

        # json_body = [
        #     {
        #       "measurement" : "npstudytest",
        #       "fields" : {
        #         "rx_rate" : rx_rate,
        #         "vnf_rate": vnf_rate,
        #         "vnf_perf": vnf_perf
        #       },
        #     }
        # ]
        # print(json_body)
        # client.write_points(json_body)
        time.sleep(1)


if __name__ == '__main__':
    main()

