FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install psycopg2-binary
COPY . .
CMD [ "python3", "main.py", "prod"]