from kafka import KafkaProducer
import json
from random import randint
import random
from time import time, sleep


def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return '{}-{}-{}'.format(first, second, last)



def main():
    while True:
        producer = KafkaProducer(
            bootstrap_servers='kafka-broker:9092',
            key_serializer=lambda k:json.dumps(k).encode('utf-8'),
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send('calls', key=random_phone_num_generator(), value={'msg':[time(), randint(1,7200), random_phone_num_generator()]})
        sleep(2)

if __name__ == '__main__':
    main()