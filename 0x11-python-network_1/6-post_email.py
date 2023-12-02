#!/usr/bin/python3
"""Send POST request to a URL with a given email.
Usage: ./6-post_email.py <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}

    response = requests.post(url, data=value)
    print(response.text)
