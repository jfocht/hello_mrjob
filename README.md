AWS Elastic Map Reduce Quickstart
=================================

This document contains scripts and code that follow the mrjob Quickstart
tutorial.

Getting Started
---------------

Sourcing develop.sh will create a virtual environment and download all
dependencies.

    $ . develop.sh

Running a Job
-------------

First, export the AWS credentials to the environment and then run the job on
AWS.

    $ export AMAZON_ACCESS_KEY_ID={key_id}
    $ export AMAZON_SECRET_ACCESS_KEY={secret_key}
    $ python word_count.py -r emr README.md
