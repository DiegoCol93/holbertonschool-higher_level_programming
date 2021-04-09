#!/bin/bash 
# Sends a POST request using the data of a json file.
curl -s "$1" --data @"$2" -H "Content-Type:application/json"
