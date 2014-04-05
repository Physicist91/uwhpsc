"""
This is a modified version of the code discussed in Lab 2 as a starting
point for Homework 1.

qroots has been modified to return real or complex roots.

plotq has been modified to plot the quadratic function as a function of
a real variable x and the real part of the roots.  

The homework problem is to modify plotq so that it shows a different plot
if the roots are complex, namely the location of the roots in the complex plane.
"""

from pylab import *

def qroots(a,b,c):
    """
    Return complex roots too.
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        # make it a complex number by adding 0j so sqrt returns complex values.
        # in Python, j is the used for sqrt(-1)
        discriminant = discriminant + 0j
    s = sqrt(discriminant)
    z0 = (-b - s) / (2*a)
    z1 = (-b + s) / (2*a)
    return z0,z1

def plotq(a,b,c):
    z0,z1 = qroots(a,b,c)
    x0 = real(z0)
    y0 = imag(z0)
    x1 = real(z1)
    y1 = imag(z1)

    # choose limits to include segment containing roots:
    xlower = min(x0, x1) - 1
    xupper = max(x0, x1) + 1
    x = linspace(xlower, xupper, 1000)

    plot(x, a*x**2 + b*x + c, 'b')   # plot quadratic with blue line
    plot([xlower,xupper], [0,0], 'k')  # plot x-axis as black line
    plot([x0,x1], [0,0], 'ro')  # plot roots as red dots

    # add a title:
    title("a = %g,  b = %g,  c = %g" % (a,b,c))


        
