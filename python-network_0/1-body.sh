#!/bin/bash
# Sends a GET request and displays body if 200 status code, else shows redirection count.
response=$(curl -s -L -w "%{http_code}" -o /tmp/response.txt "$1")
[ "$response" -eq 200 ] && cat /tmp/response.txt || echo "Redirection count: $(grep -c 'HTTP/1.1 3' /tmp/response.txt)"
