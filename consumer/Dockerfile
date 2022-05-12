FROM python:3.7-alpine
MAINTAINER Yannis Fraimis ioannis.fraimis@gmail.com

WORKDIR /app

#Install requirement
RUN pip3 install kafka-python

EXPOSE 5000

COPY src .

ENTRYPOINT ["python3", "consumer.py", "--min_duration", "100"]

