FROM python:3.6-stretch

RUN useradd -ms /bin/bash flask_app
WORKDIR /home/flask_app

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install --upgrade setuptools
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY ml ml
COPY models models
COPY data data
COPY entry.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP entry.py

RUN chown -R flask_app:flask_app ./
USER flask_app


EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
