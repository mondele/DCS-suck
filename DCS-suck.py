#!/home/jdwood/anaconda3/bin/python
# coding=<UTF-8>

#version 0.1
# by John Wood -- for Tech Advance
# This script takes a Door43 Content Service (DCS) username and downloads all repos for that user
# into the current directory (creating subdirectories for each repo as normal).
#
# It uses command-line git on the system, so that should be installed.
# Usage python3 DCS-suck.py <username>

#Import necessary python components

import requests
import json
import os
import sys

arguments=sys.argv[1:]
count_args=len(arguments)
print("DCS-suck - to pull down all repos from a DCS user. © 2020\n")
if count_args!=1: #If there is not exactly one argument, fail with a usage remark.
    if count_args == 0:
        print ("DCS-suck.py script to download all repos from a DCS user")
        print("Usage: python3 DCS-suck.py <username>")
    elif count_args > 1:
        print ("DCS-suck.py currently only handles one username at a time.")
        print ("If you are trying to specify a destination, please run this command")
        print ("    from the destination directory")
    sys.exit(1)

userName=sys.argv[1]


testUrl = "https://git.door43.org/api/v1/users/"

useUrl = testUrl + userName + "/repos"

response = requests.get(useUrl)

myObj = json.loads(response.content)

for repo in myObj:
    cloneCommand = 'git clone ' + repo["clone_url"]
    os.system(cloneCommand)
