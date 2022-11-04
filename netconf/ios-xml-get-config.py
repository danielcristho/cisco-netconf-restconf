from ncclient import manager
import xml.dom.minidom

host = "sandbox-iosxe-latest-1.cisco.com"
username = "developer"
password = "C1sco12345"
port = 830


conn = manager.connect(host=host, port=port, 
                    username=username, password=password, 
                    hostkey_verify=False, device_params={'name': 'csr'}, allow_agent=False, look_for_keys=False)

output = (conn.get_config('running'))

print(xml.dom.minidom.parseString(output.xml).toprettyxml())

conn.close_session()