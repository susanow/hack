#!/bin/sh

echo "Create vNIC in NFVi0"
export SSN_HOST=192.168.122.100
ssnctl port alloc pci0 pci 0000:00:06.0
ssnctl port alloc pci1 pci 0000:00:07.0
ssnctl port alloc vir0 virt
ssnctl port alloc vir1 virt
ssnctl ppp  alloc ppp0 vir0 vir1

echo "Create vNIC in NFVi1"
export SSN_HOST=192.168.122.101
ssnctl port alloc pci0 pci 0000:00:06.0
ssnctl port alloc pci1 pci 0000:00:07.0

echo "Create VNFs and Config them in NFVi0"
export SSN_HOST=192.168.122.100
ssnctl vnf alloc vnf0 l2fwd1b
ssnctl vnf alloc vnf1 l2fwd1b
ssnctl vnf attachport vnf0 0 pci0
ssnctl vnf attachport vnf0 1 vir0
ssnctl vnf attachport vnf1 0 vir1
ssnctl vnf attachport vnf1 1 pci1

echo "Deploy VNFs them in NFVi0"
export SSN_HOST=192.168.122.100
ssnctl vnf reset vnf0
ssnctl vnf reset vnf1
ssnctl d2 deploy vnf0
ssnctl d2 deploy vnf1


echo "Install OFRules to ovs0"
BR=ovs0
sudo ovs-ofctl del-flows  $BR
sudo ovs-ofctl add-flow   $BR in_port=1,actions=output:3
sudo ovs-ofctl add-flow   $BR in_port=3,actions=output:1
sudo ovs-ofctl add-flow   $BR in_port=2,actions=output:4
sudo ovs-ofctl add-flow   $BR in_port=4,actions=output:2
sudo ovs-ofctl add-flow   $BR actions=drop


