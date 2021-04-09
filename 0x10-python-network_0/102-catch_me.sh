#!/bin/bash
# Catches the page in the challenge.
curl "$1" -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool"
