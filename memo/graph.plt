#!/usr/local/bin/gnuplot

set terminal png
set output "/tmp/out.png"
# set xlabel "Packet Size [byte]"
# set ylabel "Throughput [Mbps]"
# set xrange [0:1200]
# set yrange [0:21000]
# set xtics (64, 128, 256, 512, 1024)

plot \
	"pktgen.dat" using 1:2 title "flow0" with lp linestyle 2, \
	"pktgen.dat" using 1:3 title "flow1" with lp linestyle 5, \
	"pktgen.dat" using 1:6 title "tpr"   with lp linestyle 7, \

