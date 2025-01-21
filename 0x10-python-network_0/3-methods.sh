#!/bin/bash
# script that prints the allowed methods in a web request
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
