import os

def frontend():
    if os.system('NODE_ENV="development" REACT_APP_API_BASE="http://localhost:5000" npm start --prefix frontend'):
        raise RuntimeError('Could not launch frontend')

def services():
    if os.system('gunicorn "app:create_app()" --bind "localhost:5000" --access-logfile - --error-logfile -'):
        raise RuntimeError('Could not launch docker-compose')

def start():
    if os.system('docker-compose -f etc/docker-compose.yml up -d'):
        raise RuntimeError('Could not launch docker-compose')

actions = {
    'frontend': frontend,
    'services': services,
    'start': start,
}
