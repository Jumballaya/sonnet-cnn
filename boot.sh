#!/bin/bash
source venv/bin/activate

# If there is an attached DB, wait until we can connect to it and run an upgrade
if [ -z "${DATABASE_URL}" ]; then
  echo "No attached database"
else
  while true; do
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
    sleep 5
  done
fi

# If we are in debug mode, run the development server
if [ $FLASK_DEBUG == 1 ]; then
  exec flask run --host=0.0.0.0 --port=5000
else
  exec gunicorn entry:app --bind '0.0.0.0:5000' --access-logfile - --error-logfile -
fi

