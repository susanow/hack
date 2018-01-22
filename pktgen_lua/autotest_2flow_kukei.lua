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

function flip(b, left, right)
	if (b) then
		return left
	else
		return right
	end
end

function traffic_test(test_times, T, tick)
	pktgen.clr();
	pktgen.start('0-1');
	pktgen.start('2-3');
	PI = 3.14
	flag = true
	for i=0, test_times, 1 do
		for j=0, T, 1 do
			tr1 = flip(flag     , 55, 8)
			tr2 = flip(not(flag), 55, 8)
			pktgen.set('0-1', 'rate', tr1)
			pktgen.set('2-3', 'rate', tr2)
			print('do')
			pktgen.delay(tick)
		end

		pktgen.delay(tick)
		pktgen.set('0-1', 'rate', flip(flag     , 40, 20))
		pktgen.set('2-3', 'rate', flip(not(flag), 40, 20))
		pktgen.delay(tick)
		pktgen.set('0-1', 'rate', flip(flag     , 28, 28))
		pktgen.set('2-3', 'rate', flip(not(flag), 28, 28))
		pktgen.delay(tick)
		pktgen.set('0-1', 'rate', flip(flag     , 20, 40))
		pktgen.set('2-3', 'rate', flip(not(flag), 20, 40))
		pktgen.delay(tick)

		flag = not(flag)
		print('flip')
	end
	pktgen.stop('0-1');
	pktgen.stop('2-3');
	return
end


print('\n\n')
print('[+] Setting Traffic Configuraton...')
pktsize = 128
test_times = 3
T = 15
tick = 2500
setting(pktsize)

print('\n\n')
print('[+] start Traffic test...')
local cnt, tr_array, tpr_array = traffic_test(test_times, T, tick)

print('fin')

-- print('\n\n')
-- print('[+] Out Test Results to File...')
-- local fname = string.format('/home/slank/pktgen_pkt%d.dat', pktsize)
-- local f = io.open(fname, 'w')
-- local fmt = '#####    %-5s  %-5s\n'
-- str = fmt:format('flow0', 'tpr1')
-- f:write(str)
-- for i=1, cnt, 1 do
-- 	local fmt  = '%05d,  %05d, %05d\n'
-- 	local tr   = tr_array[i]
-- 	local tpr = tpr_array[i]
-- 	local str  = fmt:format(i, tr, tpr)
-- 	f:write(str)
-- end
--
-- f:close()
-- print('\n\nok')

return



