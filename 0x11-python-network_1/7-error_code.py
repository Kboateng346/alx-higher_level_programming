#!/usr/bin/python3
"""Send request to a URL and display the response body.
Usage: ./7-error_code.py <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
