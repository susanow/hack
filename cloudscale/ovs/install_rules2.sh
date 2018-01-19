#!/bin/sh

BR=ovs0
ovs-ofctl del-flows  $BR
ovs-ofctl add-flow   $BR in_port=1,actions=output:2
ovs-ofctl add-flow   $BR in_port=2,actions=output:1
# ovs-ofctl add-flow   $BR in_port=3,actions=output:4
# ovs-ofctl add-flow   $BR in_port=4,actions=output:3
ovs-ofctl add-flow   $BR actions=drop
ovs-ofctl dump-flows $BR

