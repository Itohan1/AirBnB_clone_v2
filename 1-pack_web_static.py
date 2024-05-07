#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents"""
from fabric import task


def do_pack():
    web_folder = 'web_static'

    now = datetime.now()
    timestamp = now.strftime('%Y%m%d%H%M%S')

    achive_name = f'web_static_{timestamp}.tgz'

    versions_folder = 'versions'
    os.makedirs(versions_folder, exists_ok=True)

    result = c.local(f'tar - cvzf {versions_folder}/{archive_name} {
            web_folder}')

    if result.ok:
        archive_path = os.path.join(versions_folder, archive_name)
        return archive_path

    else:
        return None
