import re

re_bracket = re.compile(r'\[(.+?)\]+')
# needed some help with this one
re_outside = re.compile(r'([^[\]]+)(?:$|\[)')

def isABBA(s):
	return s[0] == s[3] and s[1] == s[2] and s[0] != s[1]

def scanSentence(s):
	if len(s)<4:
		return False
	for i in xrange(0,len(s)-3):
		if isABBA(s[i:i+4]):
			return True
	return False

tls_ips = 0

with open('ips.txt') as f:
	for l in f:
		l = l.strip()
		brackets = re_bracket.findall(l)
		outsides = re_outside.findall(l)

		print l
		flag = False
		# check inside brackets first
		for b in brackets:
			if scanSentence(b):
				print "bracket: ",b,"\n"
				flag = True
				break
		if flag:
			continue

		for o in outsides:
			if scanSentence(o):
				tls_ips+=1
				print "outside: ",o,"\n"
				break	

	print tls_ips
