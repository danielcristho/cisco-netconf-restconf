from ncclient import manager

host = "sandbox-iosxe-latest-1.cisco.com"
username = "developer"
password = "C1sco12345"
port = 830

conn = manager.connect(host=host, port=port, 
                    username=username, password=password, 
                    hostkey_verify=False, device_params={'name': 'csr'}, allow_agent=False, look_for_keys=False)

CONFIGURATION = """
<config>
<interfaces
	xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
		<name>GigabitEthernet2</name>
		<type
			xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd
		</type>
		<enabled>true</enabled>
		<ipv4
			xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
			<address>
				<ip>22.22.22.2</ip>
				<netmask>255.255.255.0</netmask>
			</address>
		</ipv4>
		<ipv6
			xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
		</ipv6>
	</interface>
</interfaces>
</config>"""

DATA = conn.edit_config(CONFIGURATION,  target = 'running')
print (DATA)
conn.close_session()