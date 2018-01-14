#!/usr/bin/env python3

import susanow
nfvi = susanow.nfvi.nfvi('labnet5.dpdk.ninja')

pci0 = nfvi.alloc_port_pci('pci0', '0000:3b:00.0')
pci1 = nfvi.alloc_port_pci('pci1', '0000:3b:00.1')
if (pci0==None or pci1==None):
    print("pci port error")
    exit(-1)

vnf0 = nfvi.alloc_vnf('vnf0', 'l2fwd1b_delay')
if (vnf0==None):
    print("vnf error")
    exit(-1)

vnf0.attach_port(0, pci0)
vnf0.attach_port(1, pci1)

vnf0.reset()

