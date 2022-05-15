#
# Kafka broker with producer and consumer


 This file contains step in order to set up a simple system with a kafka broker, a message producer container and a message 
 consumer container. The set up also includes zookeeper and an init-kafka container in order to create the kafka topic.  
 Producer sends messages to kafka broker whereas consumer consumes messages and prints in standard output information related to calls whose duration is higher than 100 seconds.


1. Please make sure that Docker is already installed in the system

2. Navigate to the directory where the exercise files are downloaded.
   This directory would contain the kafka-single-node.yml file

3. Execute the following command from this directory

        docker-compose -f kafka-single-node.yml up -d

4. Check if services are up:
		docker-compose -f kafka-single-node.yml  ps

	output:
		          Name                         Command               State                           Ports
		--------------------------------------------------------------------------------------------------------------------------
		kafka-broker                /opt/bitnami/scripts/kafka ...   Up       0.0.0.0:29092->29092/tcp, 0.0.0.0:9092->9092/tcp
		kafka-broker_init-kafka_1   /bin/sh -c                       Exit 0
									# List topics: ...
		kafka-consumer              python3 consumer.py --min_ ...   Up       0.0.0.0:5000->5000/tcp
		kafka-producer              python3 producer.py              Up       0.0.0.0:5001->5001/tcp
		zookeeper                   /opt/bitnami/scripts/zooke ...   Up       0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp, 8080/tcp	



5. Stop containers:
	
	 	docker-compose -f kafka-single-node.yml stop

6. Stop and remove containers:
		docker-compose -f kafka-single-node.yml down