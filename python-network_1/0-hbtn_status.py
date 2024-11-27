#!/usr/bin/python3
import urllib.request

# Module to fetch the status page from a specified URL and display its content
# using urllib.request, following the specific formatting instructions.

def fetch_status():
    """
    Fetches the content of the URL 'https://alu-intranet.hbtn.io/status' using
    urllib.request.urlopen, and displays the body of the response with a tabulated
    format.

    This function:
    - Sends an HTTP request to the given URL.
    - Retrieves the response body.
    - Decodes the response from bytes to UTF-8.
    - Prints the body with the required formatting (tabulation before the dash).
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
