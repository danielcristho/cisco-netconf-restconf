import json

import requests

url = 'http://172.16.0.2/ins'
username='admin'
password='admin'

myheaders={'content-type':'application/json-rpc'}
payload=[
    
    {    
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "hostname nx-os-1",
            "version": 1.2
        },
        "id": 1
    },
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders, auth=(username, password)).json()