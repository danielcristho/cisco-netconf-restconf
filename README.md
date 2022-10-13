# NETCONF Nexus using Python

## Set Nexus SSH

```bash
# int ethernet ..
# ip add 172.16.0.2 255.255.255.0
# no sh
# username admin password admin
# username admin role network-admin
# username admin passpharase lifetime 9999 warntime 14 gracetime 3
# ip domain-name ...
# ssh key rsa 2048
# feature shh
# exit
```

## Config NX-API

```bash
# feature nxapi
# nxapi http port 80
# nxapi sandbox
```

open browser, type the IP
