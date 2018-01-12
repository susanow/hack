package.path = package.path ..";?.lua;test/?.lua;app/?.lua;"

function setting(arg_pkt_size)
	pktgen.set_range('all', 'on')
	print('Setting Traffic Configuraton...')

	print('[+] set range mode on')
	sip_sta = '10.0.0.1'
	sip_min = '10.0.0.1'
	sip_max = '10.0.255.255'
	sip_inc = '0.0.0.1'
	pktgen.src_ip('all', 'start', sip_sta)
	pktgen.src_ip('all', 'min'  , sip_min)
	pktgen.src_ip('all', 'max'  , sip_max)
	pktgen.src_ip('all', 'inc'  , sip_inc)
	printf('[+] src.ip %s [%s to %s] inc:%s\n',
		sip_sta, sip_min, sip_max, sip_inc)

	dip_sta = '10.10.0.1'
	dip_min = '10.10.0.1'
	dip_max = '10.10.255.255'
	dip_inc = '0.0.0.1'
	pktgen.dst_ip('all', 'start', dip_sta)
	pktgen.dst_ip('all', 'min'  , dip_min)
	pktgen.dst_ip('all', 'max'  , dip_max)
	pktgen.dst_ip('all', 'inc'  , dip_inc)
	printf('[+] dst.ip %s [%s to %s] inc:%s\n',
		dip_sta, dip_min, dip_max, dip_inc)

	pktsize_sta = arg_pkt_size
	pktsize_min = arg_pkt_size
	pktsize_max = arg_pkt_size
	pktsize_inc = 0
	pktgen.pkt_size('all', 'start', pktsize_sta);
	pktgen.pkt_size('all', 'min'  , pktsize_min);
	pktgen.pkt_size('all', 'max'  , pktsize_max);
	pktgen.pkt_size('all', 'inc'  , pktsize_inc);
	printf('[+] pkt_size %d [%d to %d] inc:%d\n',
		pktsize_sta, pktsize_min, pktsize_max, pktsize_inc)
	return
end

function spcos(i)
	d = 40 * math.cos(i) + 60
	d = math.floor(d)
	return d
end

function traffic_test(test_times)
	if test_times < 1 then
		return -1
	end

	local date = os.date("*t")
	local time = date["hour"]..date["min"]..date["sec"]
	local f = io.open('/tmp/pktgen.dat', 'w')
	local fmt = '#####    %-5s  %-5s  %-5s  %-5s  %-5s\n'
	str = fmt:format('flow0', 'flow1', 'rxtr', 'txtr', 'tpr')
	printf('%s', str)
	f:write(str)

	pktgen.clr();
	pktgen.start('0-1');
	pktgen.start('2-3');
	local cnt = 0
	local sum_rx = 0
	local sum_tx = 0
	local idx = 1
	for j=0, test_times-1, 1 do
		PI = 3.14
		for i=0.0, 2*PI, 0.10 do
			local d = spcos(i)
			local e = spcos(i + PI)
			pktgen.set('0-1', 'rate', d)
			pktgen.set('2-3', 'rate', e)
			pktgen.delay(1000)

			local s = pktgen.portStats("all", "rate");
			local cur_rx = s[0]['mbits_rx'] + s[1]['mbits_rx']
                   + s[2]['mbits_rx'] + s[3]['mbits_rx']
			local cur_tx = s[0]['mbits_tx'] + s[1]['mbits_tx']
                   + s[2]['mbits_tx'] + s[3]['mbits_tx']
			sum_rx = sum_rx + cur_rx
			sum_tx = sum_tx + cur_tx
			cnt = cnt + 1

			fmt = '%-5d    %-5d  %-5d  %-5d  %-5d  %-5d\n'
			local str = fmt:format(idx, d, e, cur_rx, cur_tx, math.floor(cur_rx/cur_tx*100))
			printf("%s", str)
			f:write(str)
			f:flush()

			idx = idx + 1
		end
	end
	pktgen.stop('0-1');
	pktgen.stop('2-3');

	f:close()
	return cnt, math.floor(sum_rx/cnt), math.floor(sum_tx/cnt)
end


pktsize = 64
test_times = 4
setting(pktsize)
print('\n\n')
print('[+] start Traffic test...')
local cnt, avg_rx, avg_tx = traffic_test(test_times)
if cnt < 0 then
	print('taffic_test error')
	return
end


avg_rate = math.floor(avg_rx/avg_tx * 100)
print('\n\nResults')
print('-----------------------')
printf('pktsize  : %d[Byte]\n', pktsize)
printf('times    : %d[times]\n', test_times)
printf('avg-rx   : %d[Mbps]\n', avg_rx)
printf('avg-tx   : %d[Mbps]\n', avg_tx)
printf('proc-rate: %d[%%]\n'  , avg_rate)
print('\n')


