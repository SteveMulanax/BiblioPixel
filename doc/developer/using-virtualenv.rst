Using ``virtualenv``
-----------------------------------

Particularly as a developer, or even as someone who just tinkers with Python,
you should never install any new Python packages into the system Python (and
that includes Brew or MacPorts on the Mac).

There are many good reasons for this.

* This is the Python that the system uses for its work - you want to keep it as
  clean as possible

* You might well want to use a different version of Python to run your code -
  even have multiple versions for testing

* You want to quickly experiment with modules that you might also want to
  quickly delete

* You want to be able to give your work to others and need to know exactly
  what was installed

Enter the virtualenv!
=======================

A virtualenv is just a directory!

It contains a Python binary and installed packages.  You can create a fresh
virtualenv, use it for a task, put it aside for a while and work in another
one, go back to it and use it, then delete it, and never affect any other
part of your system.

In the virtualenv world, you no longer pollute your system Python.  Instead,
you install specific "clean" development versions of Python using the basic
Python installer from https://python.org

If you are developing for ``BiblioPixel``, we suggest installing at least
Python 3.4 (the oldest version that ``BiblioPixel`` supports) and Python 3.7
(the newest production version of Python).  ``BiblioPixel`` does not support
Python 2 at allo.

Each new virtualenv is based off one of these "clean" installations, but
installs new packages into its own directory.  This allows you to install large
packages or ones of unknown quality, examine them, and either use them or delete
them, without affecting any other project you are working in, or the system
itself.

virtualenv Installation depends on your operating system
================================================================

Search for "install virtualenv <your-system-here>`, or contact us if
you get stuck.


Using `virtualenv` in practice.
================================

You use virtualenv something like this.

0. First time only - create a directory for all your virtualenvs.
   Let's suppose it's `~/Envs`

1. When you start a new project, experiment or sketch, you create a new
   clean virtualenv (usually with the same name).  Let's suppose you want
   to create a new virtualenv named ``bp``.

.. code-block:: bash

    $ virtualenv ~/Envs/bp -p python3.7

2. Whenever you work on this project, you switch to that virtualenv

.. code-block:: bash

    $ source ~/Envs/bp/bin/activate

3. If you can't remember which virtualenv you are in, use bash's `which`:

.. code-block:: bash

    $ which python
    ~/Envs/bp/bin/python

4. If you can't remember which Python version you are using:

.. code-block:: bash

    $ python --version
    Python 3.6.6


5. When you want to go back to the system Python, deactivate the virtualenv:

.. code-block:: bash

    $ deactivate

6. You can list all the virtualens

 .. code-block:: bash

    $ ls ~/Envs/

7. Or if you have finished your project or experiment forever, you can delete
   the virtualenv:

 .. code-block:: bash

    $ deactivate
    $ rm -R ~/Envs/bp

Since they can be fairly large, hundreds of megabytes, it's definitely worth
cleaning up old virtualenvs to save disk space.
