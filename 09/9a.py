with open('msg.txt') as f:
	msg = f.readline().strip()
	
	i = 0
	n = len(msg)
	decoded_msg = ''
	while i < n:
		char = msg[i]
		if char=='(':
			# start reading forward
			control_seq = ''
			i += 1
			while msg[i] != ')':
				control_seq += msg[i]
				i += 1
			i += 1
			# parse sequence
			look,mult = map(int,control_seq.split('x'))
			decoded_msg += mult*msg[i:min(i+look,n)]
			i += look
		else:
			decoded_msg += char
			i+=1
	print decoded_msg
	print len(decoded_msg)