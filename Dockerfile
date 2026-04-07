# Use a highly optimized, lightweight Alpine Linux base image
FROM alpine:latest

# Metadata
LABEL maintainer="Your Name/Handle"
LABEL description="Lightweight Containerized Security Toolkit for IT Auditing"

# Update package index and install required dependencies
# --no-cache keeps the image size small by not storing the downloaded apk files
RUN apk update && apk add --no-cache \
    nmap \
    nmap-scripts \
    python3 \
    py3-pip \
    git \
    bash

# Clone sqlmap directly from the official repository
RUN git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git /opt/sqlmap

# Create a directory inside the container to hold our output reports
# This is the directory we will map to our host machine
RUN mkdir /reports

# Set the working directory
WORKDIR /app

# Copy your custom auditing script into the container
COPY scanner.py /app/scanner.py

# Make the python script executable
RUN chmod +x /app/scanner.py

# By default, when the container runs, it will execute the python script
ENTRYPOINT ["python3", "/app/scanner.py"]