#!/bin/sh

BR=ovs0

killall ovsdb-server ovs-vswitchd
rm   -rf /tmp/openvswitch
mkdir -p /tmp/openvswitch
rm -f /usr/local/var/run/openvswitch/conf.db

ovsdb-tool create /usr/local/var/run/openvswitch/conf.db /usr/local/share/openvswitch/vswitch.ovsschema
ovsdb-server \
	--remote=punix:/usr/local/var/run/openvswitch/db.sock \
	--remote=db:Open_vSwitch,Open_vSwitch,manager_options --pidfile --detach

ovs-vsctl --no-wait init
ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-lcore-mask=0x3f
ovs-vsctl --no-wait set Open_vSwitch . other_config:pmd-cpu-mask=0x30
ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-socket-mem=1024,0
ovs-vsctl --no-wait set Open_vSwitch . other_config:dpdk-init=true
ovs-vsctl --no-wait set Open_vSwitch . other_config:vhost-sock-dir=.
ovs-vswitchd unix:/usr/local/var/run/openvswitch/db.sock --pidfile
