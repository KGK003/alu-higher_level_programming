#!/bin/bash
# This script sends an OPTIONS request to the URL and displays the allowed HTTP methods.
curl -s -I "$1" | grep -i "Allow:" | cut -d' ' -f2-
