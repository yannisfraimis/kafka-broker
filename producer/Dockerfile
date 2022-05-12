FROM python:3.7-alpine
MAINTAINER Yannis Fraimis ioannis.fraimis@gmail.comls

WORKDIR /app

#Install requirement
RUN pip3 install kafka-python

EXPOSE 5001

COPY src .

ENTRYPOINT ["python3", "producer.py"]
