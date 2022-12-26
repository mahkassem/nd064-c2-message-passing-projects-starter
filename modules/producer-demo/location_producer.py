import json
from kafka import KafkaProducer


TOPIC_NAME = "location"
KAFKA_SERVER = "kafka-server:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

with open("demo_location.json") as f:
    location = json.load(f)
    producer.send(TOPIC_NAME, json.dumps(location).encode("utf-8"))
    print("Sent message: %s", location)
    producer.flush()
