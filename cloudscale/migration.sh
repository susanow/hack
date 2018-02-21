#!/bin/sh

echo "Undeploy VNF1 and termination... in NFVi0"
export SSN_HOST=192.168.122.100
ssnctl vnf undeploy vnf0
ssnctl vnf undeploy vnf1
ssnctl vnf detachport vnf0 1
ssnctl vnf detachport vnf1 0
ssnctl vnf detachport vnf1 1
ssnctl vnf attachport vnf0 1 pci1
ssnctl vnf reset vnf0
ssnctl d2 deploy vnf0
ssnctl vnf delete vnf1
ssnctl ppp delete ppp0
ssnctl port delete vir0
ssnctl port delete vir1

echo "Deploy VNF1... in NFVi1"
export SSN_HOST=192.168.122.101
ssnctl vnf alloc vnf1 l2fwd1b
ssnctl vnf attachport vnf1 0 pci0
ssnctl vnf attachport vnf1 1 pci1
ssnctl vnf reset vnf1
ssnctl d2 deploy vnf1


echo "Update OFRules"
BR=ovs0
sudo ovs-ofctl del-flows  $BR
sudo ovs-ofctl add-flow   $BR in_port=1,actions=output:3
sudo ovs-ofctl add-flow   $BR in_port=3,actions=output:1
sudo ovs-ofctl add-flow   $BR in_port=4,actions=output:5
sudo ovs-ofctl add-flow   $BR in_port=5,actions=output:4
sudo ovs-ofctl add-flow   $BR in_port=6,actions=output:2
sudo ovs-ofctl add-flow   $BR in_port=2,actions=output:6
sudo ovs-ofctl add-flow   $BR actions=drop

