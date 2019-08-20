#!/usr/bin/python3
# Distribute archive to web server.
from fabric.operations import put, run
from fabric.api import env
import os


env.hosts = ['35.237.114.53', '34.73.94.75']


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
