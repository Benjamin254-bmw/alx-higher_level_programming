#!/bin/bash
#takes URL and display all HTTP methods server will accept
curl -sX OPTIONS -i $1 | grep -i "Allow:" | cut -d' ' -f2-
