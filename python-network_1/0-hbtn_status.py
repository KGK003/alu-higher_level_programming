#!/usr/bin/python3
"""
This script fetches a URL and displays the body of the response.
The URL is passed as an argument to the script.
It uses the urllib package and ensures the response is printed with the required format.
"""

import urllib.request

# Define the URL to fetch
url = 'https://intranet.hbtn.io/status'

# Fetch the URL
with urllib.request.urlopen(url) as response:
    body = response.read()  # Read the response body

# Print the response body in the required format
print("Body response:")
print(f"    - type: {type(body)}")
print(f"    - content: {body}")
print(f"    - utf8 content: {body.decode('utf-8')}")
