#!/bin/bash
source venv/bin/activate

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

exec gunicorn entry:app --bind '0.0.0.0:5000' --access-logfile - --error-logfile -
