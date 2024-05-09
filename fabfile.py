#!/usr/bin/python3
"""fa file"""

from fabric.api import *
import datetime

env.use_ssh_config = True


def do_pack():
    """ tar """
    date = datetime.datetime.now()
    st = f"{date.year}{date.month}{date.day}\
{date.hour}{date.minute}{date.second}"

    try:
        local("if [ ! -d versions ]; then mkdir versions; fi")
        local(f"tar -czvf versions/web_static_{st}.tgz  web_static")
        print(f"web_static packed: versions/web_static_{st}.tgz")
        return f"versions/web_static_{st}.tgz"
    except Exception as e:
        return None


def upload():
    """ upload """
    put("0-setup_web_static.sh", "~/0-setup_web_static.sh", mode=744)
