#!/usr/local/bin/gnuplot

set terminal png
set output "fig_l2fwd1b_delay000_pkt64.png"

plot \
	"dat_l2fwd1b_delay000_pkt064.dat" using 1:2 title "Traffic-Rate"   with l linestyle 2, \
	"dat_l2fwd1b_delay000_pkt064.dat" using 1:3 title "TPR #thread=1 delay0"  with l linestyle 3, \
	"dat_l2fwd1b_delay000_pkt064.dat" using 1:4 title "TPR #thread=2 delay0"  with l linestyle 4, \
	"dat_l2fwd1b_delay000_pkt064.dat" using 1:5 title "TPR #thread=4 delay0"  with l linestyle 5, \


