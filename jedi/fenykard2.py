#Pyton 3.5.3

import sys
import os
import re
import csv
from collections import OrderedDict

def dirloop( pathd ):
	global osszes
	global holder

	for folders in os.listdir( pathd ):
		temp = pathd
		temp += folders
		if(os.path.isfile(temp)):
			file = open(temp, 'r')
			num = 0
			with open(temp, 'r') as f:
				for line in f.readlines():
					tempnum = re.search( '[0-9]+[\s]*\n', line )
					if( hasattr( tempnum, 'group' ) ):
						num += int( tempnum.group(0)  )
			holder.update({pathd[:-1]: num})
			osszes += num
		else:
			temp += '/'
			dirloop(temp)


def csv_open( csv_file ):
	global uholder
	global holder 

	with open(csv_file, newline = '\n') as csvfile:
		content = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in content:
			value = uholder.get(row[0], 0) + holder.get(row[1], 0)
			uholder.update({row[0]: value})



path = './City/Debrecen/Oktatás/Informatika/Programozás/DEIK/Prog1/Példák/Előadás/'
path2 = './City/Debrecen/Szórakozás/Könyv/Ismeretterjesztő/Informatika/'
path3 = './City/Debrecen/Oktatás/Informatika/Programozás/Tankönyv olvasás/'
csvf = 'db.csv'
osszes = 0
holder = {}
uholder = {}

dirloop( path )
dirloop( path2 )
dirloop( path3 )
csv_open( csvf )

for key, value in dict(uholder).items():
    if value == 0:
        del uholder[key]

uholder = OrderedDict( sorted( uholder.items(),  key=lambda x: (x[0]) ) )
uholder = OrderedDict( sorted( uholder.items(),  key=lambda x: (x[1]), reverse=True ) )

for key, value in uholder.items():
	print(key, end=' ')
	print(value)

