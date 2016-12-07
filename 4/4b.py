from collections import Counter
import re
from operator import itemgetter

# regexes
re_name = re.compile(r'^[a-z-]+')
re_sector = re.compile(r'[0-9]+')
re_checksum = re.compile(r'\[([a-z]{5})\]')

def offset_char(c,n):
	if c == '-':
		return " "
	return chr(97+(((bytearray(c)[0]-97) + n) % 26))

# counter
sector_counter = 0
with open("codes.txt") as f:
	for c in f:
		c = c.strip()

		name = re_name.search(c).group(0)
		sector = int(re_sector.search(c).group(0))
		checksum = re_checksum.search(c).group(1)

		cnt = Counter(name.replace("-","")).most_common()
		ret = sorted(cnt,key=itemgetter(0))
		ret = sorted(ret,key=itemgetter(1),reverse=True)

		checksum_deriv = "".join([x[0] for x in ret[:5]])

		if checksum == checksum_deriv:
			# valid code
			print sector,"".join([offset_char(x,sector) for x in name])

	
	print "DONE"