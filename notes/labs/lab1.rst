
.. _lab1:

Lab 1: Tuesday April 1, 2014
=============================

Brief overview of the class structure
-------------------------------------

See:

* :ref:`class_format`
* :ref:`computing_options`
* `Canvas page <https://canvas.uw.edu/courses/893991>`_
* `honor code <https://canvas.uw.edu/courses/893991/wiki/honor-code>`_

Things to try in groups:
------------------------

Please work together in groups of 2 or 3.

* Log on to `SageMathCloud <https://cloud.sagemath.com/>`_.
  See :ref:`smc`.

* Create a new project and share it with your group members.

* Open a terminal window.  If people in your group aren't comfortable with
  Unix, try out commands like *ls*, *pwd*, *mkdir*, *mv*, *cp*, etc.
  See :ref:`unix`.

* Create and edit a new file named *hello.py* by typing::

    $ open hello.py

  at the terminal prompt `$`.

* Add one line to this file and then click Save::

    print "Hello World!"

* In the terminal window, type::

    $ python hello.py

  In should print out Hello World!
  

* Edit the file to add the lines::

    import matplotlib        # python plotting package
    matplotlib.use("Agg")    # so plot commands work in this script
    from pylab import *      # imports lots of things like linspace, sin, plot

    x = linspace(0,1,1001)
    y = sin(10 * pi * x**2)
    plot(x,y)

    fname = "myplot.png"
    savefig(fname)
    print "Saved ",fname


* Save the file and rerun it at the terminal prompt, then view the file::

    $ python hello.py
    $ open myplot.png


* Open an IPython Notebook from the New menu.

* Follow the instructions for "making a plot in IPython" from the page
  :ref:`smc`.

