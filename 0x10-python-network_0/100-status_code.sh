#!/bin/bash
#Sends request to URL and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
