#!/usr/bin/python3
import urllib.request

# URL to fetch
url = "https://alu-intranet.hbtn.io/status"

# Use 'with' statement to open the URL
with urllib.request.urlopen(url) as response:
    # Read the response body
    body = response.read()
    
    # Print the body with the required tabulation before the dash
    print(f"Body response:\n\t- {body.decode('utf-8')}")
