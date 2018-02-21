#!/usr/bin/env python3
#
# MIT License
# Copyright (c) 2018 Susanow
# Copyright (c) 2018 Hiroki SHIROKURA
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

import math,time,sys
import susanow
from influxdb import InfluxDBClient
from pprint import pprint


susanow_host    = "labnet5.dpdk.ninja"
susanow_port    = 8888
influxdb_host   = "labnet5.dpdk.ninja"
influxdb_port   = 8086
influxdb_user   = 'root'
influxdb_pass   = 'root'
influxdb_dbname = 'example'
measur_id_vnfs    = 0
measur_id_ports   = 1
measur_id_cpus    = 2
measur_name_vnfs  = "vnfs"
measur_name_ports = "ports"
measur_name_cpus  = "cpus"


def get_cpus(nfvi):

    import requests
    url =  'http://' + nfvi._host + ':8888' + '/system/cpu'
    json = requests.get(url).json()
    print('{:3} {:3} {:8} {:4}'.format('soc', 'lid', 'state', 'rate'))
    n_cpu = json['n_cpu']
    ret_cpus = []
    for i in range(n_cpu):
        get_cpu = json[str(i)]
        ret_cpu = {}
        ret_cpu["id"] = "{:02}".format(i)
        ret_cores = []
        n_core = get_cpu['n_core']
        for j in range(n_core):
            get_core = get_cpu[str(j)]
            ret_core = {}
            ret_core["id"     ] = "{:02}".format(j)
            ret_core["usage"  ] = get_core["usage_rate"]
            ret_core["lcoreid"] = get_core["lcore_id"]
            ret_core["sockid" ] = get_core["socket_id"]
            ret_cores.append(ret_core)
        ret_cpu["cores"] = ret_cores
        ret_cpus.append(ret_cpu)
    return ret_cpus


def main():

    nfvi = susanow.nfvi.nfvi(susanow_host, susanow_port)
    influxdb_client = InfluxDBClient(
                 host=influxdb_host,
                 port=influxdb_port,
                 username=influxdb_user,
                 password=influxdb_pass,
                 database=influxdb_dbname)
    influxdb_client.create_database(influxdb_dbname)

    while True:
        nfvi.sync()
        json = [
            {
              "measurement" : measur_name_vnfs,
              "fields" : { "dum0":0, "dum1":1 },
            },
            {
              "measurement" : measur_name_ports,
              "fields" : { "dum0":0, "dum1":1 },
            },
            {
              "measurement" : measur_name_cpus,
              "fields" : { "dum0":0, "dum1":1 },
            },
        ]

        vnfs = nfvi.list_vnfs()
        for vnf in vnfs:
            json[measur_id_vnfs]["fields"][vnf.name() + "_rx"   ] = vnf.rxrate()
            json[measur_id_vnfs]["fields"][vnf.name() + "_tpr"  ] = vnf.tpr()
            json[measur_id_vnfs]["fields"][vnf.name() + "_ncore"] = vnf.n_core()
            traffic_ok = math.floor(vnf.rxrate() * vnf.tpr() /100.0)
            json[measur_id_vnfs]["fields"][vnf.name() + "_traffok"] = traffic_ok

        ports = nfvi.list_ports()
        for port in ports:
            json[measur_id_ports]["fields"][port.name() + "_orxp"] = port.outer_rxp()
            json[measur_id_ports]["fields"][port.name() + "_otxp"] = port.outer_txp()
            json[measur_id_ports]["fields"][port.name() + "_irxp"] = port.inner_rxp()
            json[measur_id_ports]["fields"][port.name() + "_itxp"] = port.inner_txp()

        cpus = get_cpus(nfvi)
        for cpu in cpus:
            for core in cpu["cores"]:
                corename0 = "cpu" + cpu["id"] + "_"
                corename1 = core["id"] + "_lcore" + "{:02}".format(core["lcoreid"])
                corename = corename0 + corename1
                json[measur_id_cpus]["fields"][corename + "_usage"  ] = core["usage"]
                # json[measur_id_cpus]["fields"][corename + "_lcoreid"] = core["lcoreid"]
                # json[measur_id_cpus]["fields"][corename + "_sockid" ] = core["sockid"]

        print("---------------------------------")
        pprint(json)
        influxdb_client.write_points(json)
        time.sleep(1)


if __name__ == '__main__':
    main()


