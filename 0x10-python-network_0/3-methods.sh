#!/bin/bash
# Shows all the Verbs allowed at the given ip.
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{print $2}'
