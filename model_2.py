file=open("running-config.cfg")
new_file=open("replaced.cfg",'a+')
def list_ifname_ip(file):
	for line in file:
		if "ip address" in line:
			if "no" not in line:
				line=line.strip()
				if "ip address" in line:
					ipaddress=line.split()
					ipaddress[2]=ipaddress[2].replace('192','10')
					ipaddress[2]=ipaddress[2].replace('172','10')
					ipaddress[3]=ipaddress[3].replace('255.255.255.0','255.0.0.0')
					ipaddress[3]=ipaddress[3].replace('255.255.0.0','255.0.0.0')
					new_file.write(str(ipaddress))
		else:
			new_file.write(line) 
list_ifname_ip(file)




