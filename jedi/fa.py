#Pyton 3.5.3

import sys
import os
import re

def dirloop( pathd ):
	global osszes
	for folders in os.listdir( pathd ):
		temp = pathd
		temp += folders
		if(os.path.isfile(temp)):
			file = open(temp, 'r')
			print(temp, end=' ')
			num = 0
			with open(temp, 'r') as f:
				for line in f.readlines():
					tempnum = re.search( '[0-9]+[\s]*\n', line )
					if( hasattr( tempnum, 'group' ) ):
						num += int( tempnum.group(0)  )
			print(num)
			osszes += num
		else:
			temp += '/'
			dirloop(temp)
	return ''


path = sys.argv[1]
osszes = 0

dirloop( path )
print("Összesen: ", end='')
print(osszes)