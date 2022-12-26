import json
import threading
from app.udaconnect.services import LocationService
import logging
from kafka import KafkaConsumer

TOPIC_NAME = "location"
KAFKA_SERVER = "kafka-server:9092"

logger = logging.getLogger("kafka")
logger.setLevel(logging.INFO)

processed_messages = set()


class LocationConsumer:
    def __init__(self, app):
        self.app = app
        self.consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_SERVER,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        )

        logger.info("========================================================")
        logger.info("========================================================")
        logger.info("================= LocationConsumer =====================")
        logger.info("=================== initialized ========================")
        logger.info("========================================================")
        logger.info("========================================================")

        task = threading.Thread(target=self.consume)
        task.start()

    def consume(self):
        while True:
            try:
                for message in self.consumer:
                    with self.app.app_context():
                        LocationService.create(message.value)
                    logger.info("Processed message: %s", message.value)
            except Exception as error:
                logger.error("Error consuming messages: %s", error)
