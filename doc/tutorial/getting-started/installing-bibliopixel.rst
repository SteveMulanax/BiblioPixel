Installing BiblioPixel
--------------------------------

BiblioPixel is a combination of a Python 3 library named BiblioPixel and a
command line program named ``bp``.

BiblioPixel is installed from the command line by typing:

.. code-block:: bash

   $ pip3 install -U bibliopixel

If you get a "Permission Denied" error then you need to run this command with
``sudo``\ :

.. code-block:: bash

   $ sudo pip3 install -U bibliopixel

If you get an error like "pip3: command not found" then you need to then install
Python 3 before you continue.

Download Python 3 from `here <https://www.python.org/downloads/>`_\ , and then try
the instructions above again.

Testing the installation.
^^^^^^^^^^^^^^^^^^^^^^^^^

To test your installation, type

.. code-block:: bash

   $ bp demo matrix

and it will open a browser session with an animation controlled by the command
line.

To stop ``bp``, hold down the Control key on your keyboard, then press C
(control-c).

.. bp-code-block:: footer

   shape: [64, 16]
   animation: $bpa.matrix.MatrixRain
