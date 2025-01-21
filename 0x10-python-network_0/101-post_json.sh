#!/bin/bash
# script that sends a JSON POST request to a URL passed as the first argument, and displays whether it's valid
curl -s -X POST -H "Content-Type: application/json" "$1" --data @"$2"
