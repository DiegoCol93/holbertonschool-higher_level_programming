#!/bin/bash
# GETS the content-lenght of the given IP.
curl -sI "$1"| grep -i Content-Lenght | awk '{print $2}'
