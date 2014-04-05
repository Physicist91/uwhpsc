
"""
Driver code to exercise the functions defined in hw1.py.
Change the coefficients a,b,c  and run this code to see if 
hw1.py is working properly.  

You can run at the linux command line by:
    $ python run_hw1.py
and then 
    $ open roots_plot.png
to examine the plots produced.
"""

import matplotlib
matplotlib.use("Agg")   # for making plots from script

from pylab import *
import hw1

# coefficients -- 
a = 1.
b = 2.
c = 3.

z0,z1 = hw1.qroots(a,b,c)
x0 = real(z0)
y0 = imag(z0)
x1 = real(z1)
y1 = imag(z1)

print "a = %g,  b = %g,  c = %g" % (a,b,c)
print "The roots are: "
if y0 == 0:
    print "   z0 = %g" % x0
    print "   z0 = %g" % x1
else:    
    print "   z0 = %g + %gj" % (x0,y0)
    print "   z1 = %g + %gj" % (x1,y1)

hw1.plotq(a,b,c)  # should create a plot

fname = 'roots_plot.png'
savefig(fname)
print "Created %s"  % fname

