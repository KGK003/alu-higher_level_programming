#!/bin/bash
# Sends a GET request and displays only the body of a 200 status code response.
response=$(curl -s -w "%{http_code}" -o temp_response.txt "$1") [ "${response: -3}" == "200" ] && cat temp_response.txt
