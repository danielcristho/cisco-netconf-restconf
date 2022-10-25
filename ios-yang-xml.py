from ncclient import manager
import xml.dom.minidom

host = "sandbox-iosxr-1.cisco.com"
username = "admin"
password = "C1sco12345"
port = 830

yang_file = "yang-interfaces.xml"

conn = manager.connect(host=host, port=port, username=username, password=password, hostkey_verify=False, device_params={'name': 'default'}, allow_agent=False, look_for_keys=False)

with open(yang_file) as f: 
    output = (conn.get_config('running', f.read()))

print(xml.dom.minidom.parseString(output.xml).toprettyxml())