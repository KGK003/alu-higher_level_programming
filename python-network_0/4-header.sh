#!/bin/bash
# This script sends a GET request with a custom header and displays the body of the response.
response=$(curl -s -H "X-HolbertonSchool-User-Id: 98" "$1") [ "$response" == "NOP" ] && echo "OK"
