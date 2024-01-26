#!/usr/bin/python3
"""takes a URL and an email address
-sends POST request to URL with email as a parameter
-displays the body of the response
"""
import sys
import urllib.request

if __name__ == '__main__':
    html = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(html.text)
