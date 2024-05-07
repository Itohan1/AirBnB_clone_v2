#!/usr/bin/python3
"""Write a Fabric script that generates a
tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Write a Fabric script tht generate contents"""

    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + timestamp + ".tgz"
    result_archive = local(f"tar -czvf versions/{archive_name} web_static")

    if result.succeeded:
        return (f"web_static/{archive_name}")
    else:
        return (None)
