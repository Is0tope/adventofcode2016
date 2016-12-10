import md5

door_name = "cxdnnyjw"
cnt = 0
password = 8*["_"]
print password
found_chars = 0

while found_chars<8:
	hsh = md5.new(door_name+str(cnt)).hexdigest()
	if "00000" == hsh[:5]:
		print "Found hash: ",hsh
		index,value = hsh[5:7]
		index = bytearray(index)[0]-48
		if index < 8:
			if password[index] == "_":
				password[index] = value
				print "PASSWORD: " + "".join(password)
				found_chars+=1
	cnt+=1

print "FINAL PASSWORD", password