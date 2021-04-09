#!/bin/bash
# Returns the status code of the GET response.
curl -sw -o /dev/null "%{http_code}" "$1"
