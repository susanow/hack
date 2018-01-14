package.path = package.path ..";?.lua;test/?.lua;app/?.lua;"

function setting(arg_pkt_size)
	pktgen.set_range('all', 'on')

	print('set range mode on')
	sip_sta = '10.0.0.1'
	sip_min = '10.0.0.1'
	sip_max = '10.0.255.255'
	sip_inc = '0.0.0.1'
	pktgen.src_ip('all', 'start', sip_sta)
	pktgen.src_ip('all', 'min'  , sip_min)
	pktgen.src_ip('all', 'max'  , sip_max)
	pktgen.src_ip('all', 'inc'  , sip_inc)
	printf('src.ip %s [%s to %s] inc:%s\n',
		sip_sta, sip_min, sip_max, sip_inc)

	dip_sta = '10.10.0.1'
	dip_min = '10.10.0.1'
	dip_max = '10.10.255.255'
	dip_inc = '0.0.0.1'
	pktgen.dst_ip('all', 'start', dip_sta)
	pktgen.dst_ip('all', 'min'  , dip_min)
	pktgen.dst_ip('all', 'max'  , dip_max)
	pktgen.dst_ip('all', 'inc'  , dip_inc)
	printf('dst.ip %s [%s to %s] inc:%s\n',
		dip_sta, dip_min, dip_max, dip_inc)

	pktsize_sta = arg_pkt_size
	pktsize_min = arg_pkt_size
	pktsize_max = arg_pkt_size
	pktsize_inc = 0
	pktgen.pkt_size('all', 'start', pktsize_sta);
	pktgen.pkt_size('all', 'min'  , pktsize_min);
	pktgen.pkt_size('all', 'max'  , pktsize_max);
	pktgen.pkt_size('all', 'inc'  , pktsize_inc);
	printf('pkt_size %d [%d to %d] inc:%d\n',
		pktsize_sta, pktsize_min, pktsize_max, pktsize_inc)
	return
end

function spcos(i)
	d = 40 * math.cos(i) + 60
	d = math.floor(d)
	return d
end

function traffic_test(test_times)
	pktgen.clr();
	pktgen.start('0-1');
	local idx = 1
	local tr_array = {}
	local tpr_array = {}
	local tr = 0
	PI = 3.14
	for i=0.0, test_times*2*PI, 0.10 do
		local s = pktgen.portStats("all", "rate");
		local cur_rx = s[0]['mbits_rx'] + s[1]['mbits_rx']
								 + s[2]['mbits_rx'] + s[3]['mbits_rx']
		local cur_tx = s[0]['mbits_tx'] + s[1]['mbits_tx']
								 + s[2]['mbits_tx'] + s[3]['mbits_tx']

		local tpr = math.floor(cur_rx/cur_tx*100)
		function isNaN( _v ) return _v~=_v end
		if (isNaN(tpr)) then tpr = 0 end

		table.insert(tr_array, tr)
		table.insert(tpr_array, tpr)
		print('insert   ', idx, tr, tpr)

		tr = spcos(i)
		pktgen.set('0-1', 'rate', tr)
		pktgen.delay(1000)
		idx = idx + 1
	end
	pktgen.stop('0-1');
	return #tr_array, tr_array, tpr_array
end




print('\n\n')
print('[+] Setting Traffic Configuraton...')
pktsize = 128
test_times = 1
setting(pktsize)

print('\n\n')
print('[+] start Traffic test...')
local cnt, tr_array, tpr_array_1thrd = traffic_test(test_times)

print('d2 outing...')
local r = os.execute('SSN_HOST=labnet5.dpdk.ninja ssnctl d2 out vnf0')
if r == nil then
	print('d2 out error')
	return
end
print('d2 outing...done')
pktgen.delay(2000)
local cnt, tr_array, tpr_array_2thrd = traffic_test(test_times)

print('d2 outing...')
local r = os.execute('SSN_HOST=labnet5.dpdk.ninja ssnctl d2 out vnf0')
if r == nil then
	print('d2 out error')
	return
end
print('d2 outing...done')
pktgen.delay(2000)
local cnt, tr_array, tpr_array_4thrd = traffic_test(test_times)

print('\n\n')
print('[+] Out Test Results to File...')
local fname = string.format('/home/slank/pktgen_pkt%d.dat', pktsize)
local f = io.open(fname, 'w')
local fmt = '#####    %-5s  %-5s  %-5s  %-5s\n'
str = fmt:format('flow0', 'tpr1', 'tpr2', 'tpr4')
f:write(str)
for i=1, cnt, 1 do
	local fmt  = '%05d,   %05d, %05d, %05d, %05d\n'
	local tr   = tr_array[i]
	local tpr1 = tpr_array_1thrd[i]
	local tpr2 = tpr_array_2thrd[i]
	local tpr4 = tpr_array_4thrd[i]
	local str  = fmt:format(i, tr, tpr1, tpr2, tpr4)
	f:write(str)
end
f:close()
print('\n\nok')


