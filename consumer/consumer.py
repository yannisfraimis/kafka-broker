from kafka import KafkaConsumer
import json
import multiprocessing
import argparse

stop_event = multiprocessing.Event()

def main():
    consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
    value_deserializer = lambda v: json.loads(v.decode('utf-8')))
    key_deserializer = lambda k:k.decode('utf-8')
    consumer.subscribe(['calls'])

    parser = argparse.ArgumentParser(description='Low call duration threshold in seconds')
    parser.add_argument('--min_duration',metavar='min_duration', type=int,
                    help='minimum call duration threshold in seconds')
    args = parser.parse_args()


    while not stop_event.is_set():    
        for message in consumer:
            if message.value['msg'][1] > args.min_duration:
                print("caller number: {} , callee number {}, call duration {}".format(message.key, message.value['msg'][2], message.value['msg'][1]))
            if stop_event.is_set():
                break
    consumer.close()

    


if __name__ == '__main__':
    main()
