file=open("running-config.cfg")
d={}
def list_ifname_ip(file):
	for line in file:
		if "no" not in line:
			line=line.strip()
			if "nameif" in line:
				key=line.split()
				print(key)
			if "ip address" in line:
				ipaddress=line.split()
				print(ipaddress)
				d[key[1]]=(ipaddress[2],ipaddress[3])
	return d
print(list_ifname_ip(file))
