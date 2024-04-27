#!/usr/bin/python3
"""fab file"""

from fabric.api import env, put, run
import os

env.hosts = ['100.25.158.57', '34.203.75.71']
env.key_filename = '~/.ssh/id_rsa'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ deploy tarball """
    if not os.path.isfile(archive_path):
        return False

    try:
        archive = archive_path.split("/")[1]
        Uncompressed_file = archive_path.split("/")[1].split(".")[0]
        put(archive_path, "/tmp/")
        run(f"mkdir -p /data/web_static/releases/{Uncompressed_file}/")
        run(f"tar -xzf /tmp/{archive} -C\
            /data/web_static/releases/{Uncompressed_file}/")
        run(f"rm /tmp/{archive}")
        run(f"mv -f\
            /data/web_static/releases/{Uncompressed_file}/web_static/*\
            /data/web_static/releases/{Uncompressed_file}/")
        run(f"rm -rf /data/web_static/releases/{Uncompressed_file}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -sf /data/web_static/releases/{Uncompressed_file}/\
            /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception as e:
        return False
