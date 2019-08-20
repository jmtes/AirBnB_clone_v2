#!/usr/bin/python3
# Create and distribute archive to web server.
from fabric.operations import run, local, put
from fabric.api import env
from datetime import datetime
import os


env.hosts = ['35.237.114.53', '34.73.94.75']


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


def do_deploy(archive_path):
    try:
        if not os.path.exists(archive_path):
            return False
        remote_path = '/tmp/' + archive_path[9:]
        uncom_folder = '/data/web_static/releases/' + archive_path[9:-4] + '/'
        print("Executing task 'do_deploy'")
        put(archive_path, remote_path)
        run('mkdir -p {:s}'.format(uncom_folder))
        run('tar -xzf {:s} -C {:s}'.format(remote_path, uncom_folder))
        run('rm {:s}'.format(remote_path))
        run('mv {:s}web_static/* {:s}'.format(uncom_folder, uncom_folder))
        run('rm -rf {:s}web_static'.format(uncom_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {:s} /data/web_static/current'.format(uncom_folder))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    packed = do_pack()
    if not packed:
        return False
    return do_deploy(packed)
