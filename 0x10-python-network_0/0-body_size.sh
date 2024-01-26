#!/bin/bash
# Display size of the boy of a response
curl -s -I $1 | grep -i "^Content-Length:" | awk '{print $2}'
