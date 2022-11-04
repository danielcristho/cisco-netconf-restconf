from ncclient import manager, xml_

host = "sandbox-iosxe-latest-1.cisco.com"
username = "developer"
password = "C1sco12345"
port = 830

conn = manager.connect(host=host, port=port, 
                    username=username, password=password, 
                    hostkey_verify=False, device_params={'name': 'csr'}, allow_agent=False, look_for_keys=False)


SAVE_CONFIG = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

OUTPUT = conn.dispatch(xml_.to_ele(SAVE_CONFIG))
print(OUTPUT)

conn.close_session()