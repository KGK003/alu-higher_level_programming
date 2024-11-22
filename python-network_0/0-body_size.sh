#!/bin/bash
# This script takes in a URL, sends a request, and displays the size of the response body in bytes.

# Check if the URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request using curl and display the size of the response body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
