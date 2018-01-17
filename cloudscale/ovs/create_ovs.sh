#!/bin/sh

BR=ovs0

ovs-vsctl del-br $BR

ovs-vsctl add-br $BR -- set bridge $BR datapath_type=netdev

ovs-vsctl add-port $BR dpdk0 -- \
	set Interface dpdk0 type=dpdk \
	options:dpdk-devargs=0000:3b:00.0

ovs-vsctl add-port $BR dpdk1 -- \
	set Interface dpdk1 type=dpdk \
	options:dpdk-devargs=0000:3b:00.1

ovs-vsctl add-port $BR vhost_user0 -- \
	set Interface vhost_user0 type=dpdkvhostuser

ovs-vsctl add-port $BR vhost_user1 -- \
	set Interface vhost_user1 type=dpdkvhostuser

ip link set $BR up

# options:vhost-server-path=/tmp/vhost_user0
# options:vhost-server-path=/tmp/vhost_user1

