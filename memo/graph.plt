#!/usr/bin/gnuplot

set terminal png
set output "out.png"

plot \
	"pktgen.dat" using 1:2 title "flow0" with l linestyle 2, \
	"pktgen.dat" using 1:5 title "tpr"   with l linestyle 7, \


