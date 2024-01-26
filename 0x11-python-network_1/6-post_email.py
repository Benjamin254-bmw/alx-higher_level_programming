#!/usr/bin/python3
"""takes a URL and an email address
sends POST request to URL with email as a parameter
displays the body of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


