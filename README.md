#
# Kafka broker with producer and consumer


 This file contains step in order to set up a simple system with one kafka broker and two simple python scripts named consumer.py and producer.py.
 producer sends messages to kafka broker whereas consumer consumes messages and prints in standard output information related to calls whose
 duration is higher than X seconds.


1. Please make sure that Docker is already installed in the system

2. Navigate to the directory where the exercise files are downloaded.
   This directory would contain the kafka-single-node.yml file

3. Execute the following command from this directory

        docker-compose -f kafka-single-node.yml up -d

4. Logging into the Kafka Container

        docker exec -it kafka-broker /bin/bash

5. Navigate to the Kafka Scripts directory

   	 	cd /opt/bitnami/kafka/bin

6. Create new topic called calls:

    	 /kafka-topics.sh --create --topic calls --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 

7. In machine wherein python scripts are going to be run we need to run as well:
		pip install -r requirements.txt

8. Open one terminal for consumer and run python consumer.py --min_duration  <your input for min call duration threshold>

9. Open terminal and run the producer, python producer.py which constantly produces messages related to kafka calls topic. Consumer print messages whose duration is greater than the value follows  --min_duration flag. 
		
10. In order to list topics in kafka:
	
		cd /opt/bitnami/kafka/bin && ./kafka-topics.sh --list  --bootstrap-server localhost:9092

11. In order to stop kafka:
	
	 	docker-compose -f kafka-single-node.yml stop
