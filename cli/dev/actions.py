import os


def run():
    if os.system('docker-compose -f etc/docker-compose.yml up -d'):
        raise RuntimeError('Could not launch docker-compose')
