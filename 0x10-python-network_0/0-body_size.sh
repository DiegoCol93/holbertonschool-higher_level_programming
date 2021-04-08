#!/bin/bash
# GETS the content-lenght of the given IP.
curl -sI "$1"| grep Content-Length | awk '{print $2}'
