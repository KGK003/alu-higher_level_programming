#!/bin/bash
# Sends a GET request with a custom header and displays "OK" if response is "NOP"
[ "$(curl -s -H "X-HolbertonSchool-User-Id: 98" "$1")" == "NOP" ] && echo -n "OK"
