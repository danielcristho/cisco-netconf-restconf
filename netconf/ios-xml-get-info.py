from ncclient import manager

host = "sandbox-iosxe-latest-1.cisco.com"
username = "developer"
password = "C1sco12345"
port = 830

conn = manager.connect(host=host, port=port, 
                    username=username, password=password, 
                    hostkey_verify=False, device_params={'name': 'csr'}, allow_agent=False, look_for_keys=False)

FILTER = """
<filter
	xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<hostname></hostname>
		<interface>
			<GigabitEthernet>
				<name>1</name>
			</GigabitEthernet>
		</interface>
	</native>
</filter>"""

print (conn.get_config('running', FILTER))
conn.close_session()