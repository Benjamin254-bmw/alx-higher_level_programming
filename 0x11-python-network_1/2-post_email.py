#!/usr/bin/python3
"""script that takes in a URL and an email
    sends a POST request to the URL as parameter
    displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        rint(response.read().decode("utf-8"))
