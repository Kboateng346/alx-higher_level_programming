#!/usr/bin/python3
"""Display X-Request-Id header of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        xRequestId = dict(response.headers).get("X-Request-Id")
        print(xRequestId)
