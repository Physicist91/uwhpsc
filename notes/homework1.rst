
.. _homework1:

==========================================
Homework 1 
==========================================

.. comment :: Not yet assigned and may change.  




The goals of this homework are to:

 * Make sure you are familiar with basic Unix commands (see :ref:`unix`)
   and an editor, (see :ref:`editors`),
 * Start using *git* (:ref:`git`) to download course materials,
 * Create your own bitbucket repository to keep your coursework
 * Make sure you have some necessary software installed.

Before tackling this homework, you should read some of the class notes and
links they point to.  In particular, the following sections are relevant:

 * :ref:`unix`
 * :ref:`software_installation`
 * :ref:`editors`
 * :ref:`git`
 * :ref:`bitbucket`
 * :ref:`biblio`

For UW students, a primary goal of this homework is to 
create a bitbucket repository to add files to that can be graded by the
course instructors.

Homework done by Coursera students will not be viewed or graded but you may
still want to follow these instructions to get yourself set up.  Parts not
relevant have been deleted from the assignment.

See also the `Bitbucket 101 instructions
<https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+101>`_ that
for more tips on setting up bitbucket accounts and using git.


 #. Make sure you have access to *git* on the computer you plan to use
    (see :ref:`software_installation`).  Read the section :ref:`git` and the
    documentation linked from there in order to get a sense of how it works.

 #. Clone the class repository following the 
    :ref:`classgit`.

    Make sure you have set the environment variable *UWHPSC*
    since this is used below.

 #. Set up your own personal repository on Bitbucket, by carefully following 
    all of the instructions at :ref:`mygit`.
    By following these instructions you will also create a clone of the
    repository and add some files to it.

    Make sure you have set the environment variable *MYHPSC*
    since this is used below.

 #. In the clone of your repository, create a subdirectory *homework1*::

        $ cd $MYHPSC
        $ mkdir homework1

    You should now be able to *cd* into this directory::

        $ cd homework1

    or later you can get there from anywhere via::

        $ cd $MYHPSC/homework1


 #. Copy some files from the class repository to your own repository by::

        $ cp $UWHPSC/codes/homework1/*  $MYHPSC/homework1

    This should create the files 
         * `test1.py`
         * `test2.sh`
         * `test3.f90`
    in the directory *$MYHPSC/homework1*.  

 #. Use `git add` and `git commit` to add these three files and commit
    a snapshot.

 #. Modify `test1.py` as instructed in the *docstring* at the top of the
    file.  Try running it via::

        $ python test1.py

    It should give results like the following::

        Code run by Your Name
        Environment variable UWHPSC is /somepath/uwhpsc
        Environment variable MYHPSC is /somepath/myhpsc
        Imported numpy ok
        Imported matplotlib ok
        Imported pylab ok

    Following the instructions, you will add and commit to files, a modified
    version of `test1.py` and the output file `test1output.txt`.

 #. Modify `test2.sh` as instructed in the comments at the top of the file.
 #. Run this bash shell script via::

        $ bash test2.sh

    This should give output something like the following::

        Environment variable UWHPSC is /somepath/uwhpsc
        Environment variable MYHPSC is /somepath/myhpsc

        which ipython returns...
        /somepath/ipython

        which gfortran returns...
        /usr/local/bin/gfortran

        gfortran --version returns...
        GNU Fortran (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3

        [more stuff]

        Compiling and running a Fortran code...
         Code run by Your Name
         Successfully ran Fortran 90 program

    Now run it again and redirect the output to a file::

        $ bash test2.sh > test2output.txt
    
    Add and commit the modified `test2.sh` and the output files to your repository.

    **Note:** At the end you should have the following files committed
    to your repository:

        * $MYHPSC/testfile.txt
        * $MYHPSC/homework1/test1.py
        * $MYHPSC/homework1/test1output.txt
        * $MYHPSC/homework1/test2.sh
        * $MYHPSC/homework1/test2output.txt
        * $MYHPSC/homework1/test3.f90

    Do **not** check in the file *a.out*, which was created when the Fortran
    code was compiled.

    Push them to bitbucket via::

        $ git push

    These files should then also be visible from your bitbucket webpage, by
    clicking on the "Source" tab, see :ref:`bitbucket`.


