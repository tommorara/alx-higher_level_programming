#!/bin/bash
# script that will display the size of the body of the response
curl -so /dev/null "$1" -w "%{size_download}"
