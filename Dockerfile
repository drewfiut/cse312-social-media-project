FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app

RUN pip install Flask==0.10.1

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
