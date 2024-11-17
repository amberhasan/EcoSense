# Use an official Python image
FROM python:3.9-slim

WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y netcat openjdk-11-jdk-headless && apt-get clean

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "api_server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
