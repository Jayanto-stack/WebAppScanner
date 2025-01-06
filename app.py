import requests
import socket
from concurrent.futures import ThreadPoolExecutor

# HTTP Header Scanner
# Get method indicates that you're trying to get or retrieve data from a specified resource.
# To make a GET request using Requests, you can invoke requests.get()
def scan_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers

    # Check for security header
        print("\nSecurity Header Analysis:")
        if "Content-Security-Policy" in headers:
            print("Content-Security-Policy is set.")
        else:
            print("Content-Security-Policy is missing.")
    
        if "X-Content-Type-Options" in headers:
            print("X-Content-Type-Options is set.")
        else:
            print("X-Content-Type-Options is missing.")
    
        if "X-Frame-Options" in headers:
            print("X-Frame-Options is set.")
        else:
            print("X-Frame-Options is missing.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Open Ports Scanning
