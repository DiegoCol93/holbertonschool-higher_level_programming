#!/bin/bash
# Returns the status code of the GET response.
curl -s -o /dev/null -w "%{http_code}" "$1"
