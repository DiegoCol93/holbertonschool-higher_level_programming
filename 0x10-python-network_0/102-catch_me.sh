#!/bin/bash
# Catches the page in the challenge.
curl 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool"
