#!/usr/bin/python3
import urllib.request
import sys

"""
This script takes a URL from the command line, sends an HTTP request to the URL, 
and prints the value of the 'X-Request-Id' header from the response.

The value of the 'X-Request-Id' header is typically unique for each request and 
is returned by the server in the response headers.

Modules used:
- urllib: To make the HTTP request and access the response headers.
- sys: To access command-line arguments (the URL).

Usage:
1. The script expects a URL as a command-line argument.
2. It sends a GET request to the URL and fetches the response headers.
3. It looks for the 'X-Request-Id' header and prints its value.

Example:
    $ python3 script.py https://example.com
    X-Request-Id: 12345abcde
"""

def fetch_request_id():
    """
    Fetches the value of the 'X-Request-Id' header from the HTTP response 
    when making a GET request to the URL provided as a command-line argument.
    The function sends the request, reads the response headers, and prints 
    the value of the 'X-Request-Id' header if it exists.

    The function uses a 'with' statement to ensure proper management of the 
    HTTP connection and response object.
    """
    # Get the URL from the command-line argument
    url = sys.argv[1]

    # Send a GET request to the URL using 'urllib.request.urlopen'
    with urllib.request.urlopen(url) as response:
        # Fetch all headers from the response
        headers = response.getheaders()
        
        # Search for 'X-Request-Id' header and print its value
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])
                return

# Call the function to fetch and display the X-Request-Id
if __name__ == "__main__":
    fetch_request_id()

