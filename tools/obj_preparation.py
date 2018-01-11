#!/usr/bin/env python3

import susanow
nfvi = susanow.nfvi.nfvi('labnet5.dpdk.ninja')

pci0 = nfvi.alloc_port_pci('pci0', '0000:3b:00.0')
pci1 = nfvi.alloc_port_pci('pci1', '0000:3b:00.1')
pci2 = nfvi.alloc_port_pci('pci2', '0000:86:00.0')
pci3 = nfvi.alloc_port_pci('pci3', '0000:86:00.1')
if (pci0==None or pci1==None or pci2==None or pci3==None):
    print("pci port error")
    exit(-1)

vnf0 = nfvi.alloc_vnf('vnf0', 'l2fwd1b')
vnf1 = nfvi.alloc_vnf('vnf1', 'l2fwd1b')
if (vnf0==None or vnf1==None):
    print("vnf error")
    exit(-1)

vnf0.attach_port(0, pci0)
vnf0.attach_port(1, pci1)
vnf1.attach_port(0, pci2)
vnf1.attach_port(1, pci3)

vnf0.reset()
vnf1.reset()

