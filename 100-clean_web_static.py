#!/usr/bin/python3
# script that deletes out-of-date archives, using the function do_clean
from fabric.api import local
from fabric.api import env
from fabric.api import run
from fabric.api import put
from datetime import datetime
import os.path

env.hosts = ['34.207.120.198', '52.201.192.135']


def do_clean(number=0):
    """Delete out-of-date archives.
    """
    number = int(number)
    local("ls -d -1tr versions/* | tail -n +{} | \
          xargs -d '\n' rm -f --".format(2 if number < 1 else number + 1))
    run("ls -d -1tr /data/web_static/releases/* | tail -n +{} | \
          xargs -d '\n' rm -rf --".format(2 if number < 1 else number + 1))
