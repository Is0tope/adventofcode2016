import md5

door_name = "cxdnnyjw"
cnt = 0
password = ""

while len(password)<8:
	hsh = md5.new(door_name+str(cnt)).hexdigest()
	if "00000" == hsh[:5]:
		password += hsh[5]
		print "Found hash: ",hsh
		print "PASSWORD: " + password + ("*"*(8-len(password)))
	cnt+=1

print "FINAL PASSWORD", password