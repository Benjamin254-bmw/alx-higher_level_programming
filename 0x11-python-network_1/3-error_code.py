#!usr/bin/python3
"""Script that:
-takes URL and sends a request to the URL
-displays the body of the response ( utf-8).
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
