from ncclient import manager

conn = manager.connect (
    host='172.16.0.2',
    port=22,
    username='admin',
    password='admin',
    device_params={'name': 'nexus'},
    look_for_keys=False
)

for value in conn.server_capabilities:
    print(value)

conn.close_session()    