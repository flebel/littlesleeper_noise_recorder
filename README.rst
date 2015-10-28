================================
Noise recorder for LittleSleeper
================================

This script records historical noise levels of a remote LittleSleeper instance.

Getting started
===============

Requirements:

* LittleSleeper
* requests
* sqlalchemy

LittleSleeper must be accessible from the system on which this software runs.

The other requirements are expressed in the `requirements.txt` file and may be
installed by running the following command (preferably from a virtual
environment)::

    pip install -r requirements.txt

Usage
=====

Execute the `runner.py` script without arguments to get the list of available parameters.

Set the `DEBUG` environment variable for verbose output, for example:

    DEBUG=1 ./runner X Y Z

