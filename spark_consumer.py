from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, FloatType, LongType
from confluent_kafka import Consumer
import json
import sys

# Reduce Spark logging verbosity
from pyspark import SparkContext
sc = SparkContext.getOrCreate()
sc.setLogLevel("ERROR")

# Initialize Spark Session
spark = SparkSession.builder.appName("KafkaSparkStreaming").getOrCreate()

# Define schema for incoming data
schema = StructType([
    StructField("building_id", StringType(), True),
    StructField("timestamp", LongType(), True),
    StructField("energy_usage", FloatType(), True),
    StructField("temperature", FloatType(), True),
    StructField("hvac_status", StringType(), True)
])

def consume_from_kafka():
    # Kafka consumer configuration
    consumer_config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'energy-spark-consumer',
        'auto.offset.reset': 'earliest'
    }

    try:
        consumer = Consumer(consumer_config)
        consumer.subscribe(['energy-topic'])
        
        while True:
            messages = []
            for _ in range(5):  # Poll up to 5 messages at a time
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    print(f"Consumer error: {msg.error()}")
                    continue

                # Decode and parse the message
                try:
                    data = json.loads(msg.value().decode('utf-8'))
                    print(f"Consumed from Kafka: {data}")
                    messages.append(data)
                except json.JSONDecodeError as e:
                    print(f"Failed to decode message: {e}")
                    continue

            if not messages:
                continue

            # Convert the list of messages to a DataFrame
            df = spark.createDataFrame(messages, schema=schema)
            df.show(truncate=False)

            # Perform real-time analytics (example: average energy usage)
            avg_usage = df.groupBy("building_id").avg("energy_usage")
            avg_usage.show(truncate=False)

    except Exception as e:
        print(f"Error in consumer: {e}")
    finally:
        consumer.close()
        print("Kafka consumer closed")

if __name__ == "__main__":
    consume_from_kafka()
