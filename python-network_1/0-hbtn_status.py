#!/usr/bin/python3
# This script fetches https://alu-intranet.hbtn.io/status and displays the body of the response

import urllib.request

# Define the URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Fetch the URL
with urllib.request.urlopen(url) as response:
    body = response.read()  # Read the response body

# Print the response body in the required format
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")