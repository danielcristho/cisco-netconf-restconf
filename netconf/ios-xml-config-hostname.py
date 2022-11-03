from ncclient import manager

host = "sandbox-iosxe-latest-1.cisco.com"
username = "developer"
password = "C1sco12345"
port = 830

conn = manager.connect(host=host, port=port, 
                    username=username, password=password, 
                    hostkey_verify=False, device_params={'name': 'csr'}, allow_agent=False, look_for_keys=False)

CONFIGURATION = """
<config
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<hostname>router1</hostname>
	</native>
</config>"""

RUN = (conn.edit_config(CONFIGURATION, target = 'running', ))
print(RUN)
conn.close_session()