#!/usr/bin/env python3

import susanow
import susanow.d2 as d2

nfvi = susanow.nfvi.nfvi('labnet5.dpdk.ninja')
vnf0 = nfvi.get_vnf('vnf0')
vnf1 = nfvi.get_vnf('vnf1')
pci0 = nfvi.get_port('pci0')
pci1 = nfvi.get_port('pci1')
pci2 = nfvi.get_port('pci2')
pci3 = nfvi.get_port('pci3')
if (vnf0==None or vnf1==None):
    print("vnf error")
    exit(-1)
if (pci0==None or pci1==None or pci2==None or pci3==None):
    print("pci port error")
    exit(-1)

vnf0.attach_port(0, pci0)
vnf0.attach_port(1, pci1)
vnf0.reset()

vnf1.attach_port(0, pci2)
vnf1.attach_port(1, pci3)
vnf1.reset()

