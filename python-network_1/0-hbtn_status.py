#!/usr/bin/python3
import urllib.request

"""
This module retrieves the body content of a web page located at the URL 
'https://alu-intranet.hbtn.io/status' using the urllib library in Python.

It follows specific requirements:
- The request is made using the `urllib.request` module.
- Only `urllib` is used, and no other external modules or packages are imported.
- The body of the HTTP response is fetched and printed with a tabulation before the dash ('-').

The script is intended to be a simple demonstration of how to fetch a web page's 
response using the `urllib` library while following a particular formatting convention.

Purpose:
    This script makes an HTTP request to a predefined URL and displays the body of 
    the response in a formatted manner. This is useful for understanding how HTTP 
    requests work in Python and for demonstrating basic interaction with web servers 
    using built-in libraries.

    The module is designed to work in an environment where only the `urllib` library 
    is available for making HTTP requests.

Usage:
    The script, when executed, will fetch the status page and print the response 
    in a human-readable format with a tabulation character before the response body.

"""

def fetch_status():
    """
    Fetches the content of the URL 'https://alu-intranet.hbtn.io/status' using
    the urllib.request.urlopen function, retrieves the response body, and prints
    the body with a tabulated format.

    This function follows these steps:
    1. Opens an HTTP connection to the specified URL.
    2. Reads the response from the server.
    3. Decodes the response from bytes into a UTF-8 string.
    4. Prints the content of the response, formatted with a tabulation character 
       before the dash ('-').

    No external packages are used in this function, and the body of the response 
    is displayed exactly as it is returned from the server, ensuring the output 
    follows the specified format.

    The function is wrapped in a `with` statement to ensure that the connection is 
    properly closed after reading the response.

    The function does not return any value, it directly prints the formatted body 
    response to the console.
    """
    
    # URL to fetch
    url = "https://alu-intranet.hbtn.io/status"

    # Use 'with' statement to open the URL and automatically close it after the block
    with urllib.request.urlopen(url) as response:
        # Read the response body
        body = response.read()

        # Print the body with the required tabulation before the dash
        print(f"Body response:\n\t- {body.decode('utf-8')}")

# Call the function to fetch and display the status page
if __name__ == "__main__":
    fetch_status()

