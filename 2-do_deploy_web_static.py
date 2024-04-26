#!/usr/bin/python3
"""fab file"""

from fabric.api import *
import datetime
import os

env.use_ssh_config = True
env.hosts = ['100.25.158.57', '34.203.75.71', ]


def do_pack():
    """ tar """
    date = datetime.datetime.now()
    st = f"{date.year}{date.month}{date.day}\
{date.hour}{date.minute}{date.second}"

    try:
        local("if [ ! -d versions ]; then mkdir versions; fi")
        local(f"tar -czvf versions/web_static_{st}.tgz  web_static/")
        print(f"web_static packed: versions/web_static_{st}.tgz")
        return f"versions/web_static_{st}.tgz"
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ deploy tarball """
    if os.path.exists(f"{archive_path}"):
        try:
            archive = archive_path.split("/")[1]
            Uncompressed_file = archive_path.split("/")[1].split(".")[0]
            put(archive_path, "/tmp/")
            run(f"mkdir -p /data/web_static/releases/{Uncompressed_file}/")
            run(f"tar -xzf /tmp/{archive} \
-C /data/web_static/releases/{Uncompressed_file}/")
            run(f"rm /tmp/{archive}")
            run(f"mv -f /data/web_static/releases/\
{Uncompressed_file}/web_static/*\
 /data/web_static/releases/{Uncompressed_file}/")
            run(f"rm -rf /data/web_static/releases/\
{Uncompressed_file}/web_static")
            run(f"rm -rf /data/web_static/current")
            run(f"ln -sf /data/web_static/releases/\
{Uncompressed_file}/ /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception as e:
            print("Blunder")
            return False
    else:
        return False


def upload():
    """ upload """
    put("0-setup_web_static.sh", "~/0-setup_web_static.sh", mode=744)
