from fastapi import FastAPI
from pydantic import BaseModel
from confluent_kafka import Consumer
import json

app = FastAPI()

# Kafka consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'energy-api-consumer',
    'auto.offset.reset': 'earliest'
}

# Initialize Kafka consumer
consumer = Consumer(consumer_config)
consumer.subscribe(['energy-topic'])

# Endpoint to get real-time energy data
@app.get("/energy")
def get_energy_data():
    msg = consumer.poll(1.0)  # Poll for new messages
    if msg is None or msg.error():
        return {"message": "No new data"}

    data = json.loads(msg.value().decode('utf-8'))
    return data

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
