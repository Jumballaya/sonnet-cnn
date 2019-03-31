FROM python:3.6.8-stretch

RUN mkdir -p /app
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "entrypoint.sh"]
