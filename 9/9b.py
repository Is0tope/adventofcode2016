	
def decode(msg,start=0,end=None):
	if end==None:
		end = len(msg)
	i = start
	n = end
	#decoded_msg = ''
	decoded_cnt = 0

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
			#decoded_msg += mult*decode(msg,i,min(i+look,n))
			decoded_cnt += mult*decode(msg,i,min(i+look,n))
			i += look
		else:
			decoded_cnt += 1
			i+=1
	return decoded_cnt

with open('msg.txt') as f:
	msg = f.readline().strip()
	D = decode(msg)
	print D
	#print len(D)