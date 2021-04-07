FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE 5434
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]