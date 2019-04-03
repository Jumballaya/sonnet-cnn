#!/bin/bash

# create virtual environment
python3 -m venv venv

# install python requirements
venv/bin/pip install -r requirements.txt

# install node requirements
npm install --prefix frontend

# alias the project command
echo 'alias project=./project' >> venv/bin/activate
