from confluent_kafka import Producer, Consumer, KafkaError
import json
import random
import time

# Kafka configuration
KAFKA_BROKER = 'localhost:9092'
TOPIC = 'energy-topic'

# Function to create a Kafka Producer
def create_producer():
    return Producer({'bootstrap.servers': KAFKA_BROKER})

# Function to produce data to Kafka
def produce_data():
    producer = create_producer()
    while True:
        # Generate random energy data
        data = {
            "building_id": f"Building_{random.randint(1, 5)}",
            "timestamp": int(time.time()),
            "energy_usage": round(random.uniform(100, 500), 2),
            "temperature": round(random.uniform(18, 30), 2),
            "hvac_status": random.choice(["ON", "OFF"])
        }
        # Send data to Kafka
        producer.produce(TOPIC, value=json.dumps(data))
        producer.flush()
        print(f"Sent: {data}")
        time.sleep(2)

# Function to create a Kafka Consumer
def create_consumer():
    return Consumer({
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'energy-consumer-group',
        'auto.offset.reset': 'earliest'
    })

# Function to consume data from Kafka
def consume_data():
    consumer = create_consumer()
    consumer.subscribe([TOPIC])
    while True:
        msg = consumer.poll(1.0)  # Poll for new messages
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() != KafkaError._PARTITION_EOF:
                print(f"Error: {msg.error()}")
            continue
        # Print the received message
        data = json.loads(msg.value().decode('utf-8'))
        print(f"Received: {data}")

# Main function to run Producer and Consumer
if __name__ == "__main__":
    from threading import Thread

    # Start Producer in a separate thread
    producer_thread = Thread(target=produce_data)
    producer_thread.start()

    # Start Consumer in the main thread
    consume_data()
