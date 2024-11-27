#!/usr/bin/python3
import urllib.request

"""
This module fetches the body of the response from the URL 
'https://alu-intranet.hbtn.io/status' using the urllib.request module.

It sends an HTTP GET request to the specified URL, retrieves the body of the 
response, and prints it formatted with a tabulation before the dash ('-').

Usage:
    $ python3 script.py
"""

def fetch_status():
    """
    Fetches the content of the URL 'https://alu-intranet.hbtn.io/status' 
    and prints the body of the response with a tabulation before the dash ('-').

    The function:
    - Sends an HTTP GET request to the URL.
    - Reads the body of the response.
    - Decodes the body in UTF-8 and prints it in the specified format.
    
    The function uses a 'with' statement to ensure proper resource management.
    """
    url = "https://alu-intranet.hbtn.io/status"
    
    # Use 'with' statement to open the URL and ensure proper closing
    with urllib.request.urlopen(url) as response:
        # Read the body of the response
        body = response.read()
        
        # Print the body with a tabulation before the dash ('-')
        print(f"Body response:\n\t- {body.decode('utf-8')}")


# Ensures the fetch_status function is called only when the script is run directly
if __name__ == "__main__":
    fetch_status()


