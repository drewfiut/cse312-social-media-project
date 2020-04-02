FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app
ENV MYSQL_PASSWORD  RNPr4UaGaK
RUN pip install Flask==0.10.1
RUN pip install mysql-connector
COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
