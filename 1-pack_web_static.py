#!/usr/bin/python3
# Generate a .tgz archive from the contents of the web_static folder.
from fabric.operations import local
from datetime import datetime
import os


def do_pack():
    try:
        d = datetime.now()
        cmd = 'tar -cvzf '
        dest = 'versions/web_static_{:d}{:d}{:d}{:d}{:d}{:d}.tgz '
        dest = dest.format(d.year, d.month, d.day, d.hour, d.minute, d.second)
        src = 'web_static'
        if not os.path.exists('versions/'):
            os.makedirs('versions/')
        local(cmd + dest + src)
        return dest
    except Exception:
        return None
