import re

re_bracket = re.compile(r'\[(.+?)\]+')
# needed some help with this one
re_outside = re.compile(r'([^[\]]+)(?:$|\[)')

def isABA(s):
	return s[0] == s[2] and s[0] != s[1]

def getABAS(s):
	if len(s)<3:
		return []
	abas = []
	for i in xrange(0,len(s)-2):
		sub = s[i:i+3]
		if isABA(sub):
			abas.append(sub)
	return abas

def invertABA(s):
	return s[1]+s[0]+s[1]

ssl_ips = 0

with open('ips.txt') as f:
	for l in f:
		l = l.strip()
		brackets = re_bracket.findall(l)
		outsides = re_outside.findall(l)

		print l

		abas = []
		for o in outsides:
			abas += getABAS(o)
		for a in abas:
			a_inv = invertABA(a)
			if any([a_inv in x for x in brackets]):
				ssl_ips += 1
				print a
				break

	print ssl_ips
