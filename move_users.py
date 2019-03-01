#! usr/bin/python3
# Allows to communicate with RESTful API to move users from one group to another.

import requests

headers = {
    'content-type': "application/json",
    'auth': 'auth'
    }

users = open('File_name_here').read().split(',')

baseurl = "URL"

# Cleanup the IDs from file.
for i in range(len(users)):
    if i == 0:
        users[i] = users[i].lstrip('[')
    elif i == len(users) - 1:
        users[i] = users[i].rstrip(']')
    users[i] = users[i].strip('",')

for item in users:
    print(item)
    print(requests.post(baseurl, headers=headers, json=[item]))
