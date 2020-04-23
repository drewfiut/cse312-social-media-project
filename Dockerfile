FROM python:3.7.5

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /app
ENV MYSQL_PASSWORD RNPr4UaGaK
RUN pip install Flask==0.10.1
RUN pip install mysql-connector
RUN pip install flask-wtf
RUN pip install flask-socketio 
RUN pip install flask-bcrypt
RUN pip install Pillow
RUN pip install flask-login
COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
