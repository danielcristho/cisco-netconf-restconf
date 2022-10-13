from urllib import response
import requests
import json

url = 'http://172.16.0.2/ins'
username='admin'
password='admin'

myheaders={'content-type':'application/json-rpc'}
payload=[
    
    {
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "interface ethernet 2/2",
            "version": 1.2
        },
        "id": 2
    },
    
    {    
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "description foo-bar",
            "version": 1.2
        },
        "id": 3
    },
    
    {    
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "end",
            "version": 1.2
        },
        "id": 4
    },
    
    {    
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "copy run start",
            "version": 1.2
        },
        "id": 5
    },
    
    {    
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "vlan 10",
            "version": 1.2
        },
        "id": 6
    },
    
    {    
        "jsonrpc": "2.0",
        "method": "cli",
        "params": {
            "cmd": "name office",
            "version": 1.2
        },
        "id": 7
    },
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders, auth=(username, password)).json()