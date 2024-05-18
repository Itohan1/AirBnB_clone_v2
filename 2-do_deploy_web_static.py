#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)"""
from fabric.api import task, Connection
from fabric.api import env, run, put, cd
import os
env.hosts = ['52.86.31.8', '52.3.47.83']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Write a Fabric script (based on the file 1-pack_web_static.py)"""
    if not os.path.exists(archive_path):
        return (False)
    with Connection(env.hosts[0], user=env.user, connect_kwargs={'key_filename': env.key_filename}) as conn:
        conn.put(archive_path, '/tmp/')

    archive_filename = archive_path.split('/')[-1]
    string = f"/data/web_static/releases/{archive_filename.split('.')[0]}"
    current = "/data/web_static/current"
    with conn.cd("/tmp"):
        conn.run(f"tar -xzvf {archive_filename} -C {string}")
        conn.run(f"rm {archive_filename}")
    conn.run("rm -rf {current}")
    conn.run(f"ln -sf {string} {current}")
    """result = local(f"scp {path}
    ubuntu@IP web-01:{current_link}
    & scp {path} ubuntu@IP web-02:{current_link} & ")"""

    return (True)
