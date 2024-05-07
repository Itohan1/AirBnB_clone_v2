#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)"""
from fabric.api import env, run, put, local
import os
env.hosts = ['<IP web-01>', 'IP web-02']
env.user = '<username>'
env.key_filename = '<path to SSH key>'


def do_deploy(archive_path):
    """Write a Fabric script (based on the file 1-pack_web_static.py)"""
    if not os.path.exists(archive_path):
        return (False)

    put(archive_path, '/tmp/')

    archive_filename = archive_path.split('/')[-1]
    string = f"/data/web_static/releases/{archive_filename.split('.')[0]}"
    current = "/data/web_static/current"
    with cd("/tmp"):
        run(f"tar -xzvf {archive_filename} -C {string}")
        run(f"rm {archive_filename}")
    run("rm -rf {current}")
    run(f"ln -sf {string} {current}")
    """result = local(f"scp {path}
    ubuntu@IP web-01:{current_link}
    & scp {path} ubuntu@IP web-02:{current_link} & ")"""

    return (True)
