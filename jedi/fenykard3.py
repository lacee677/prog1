#Pyton 3.5.3

# command line usage
# python3 fenykard3.py | gource --seconds-per-day 1.25 --highlight-users --auto-skip-seconds 1 --background 660033 --font-size 12 --title "FUTURE9, JÖVŐ DEBRECEN" --font-colour FFB3B3 --dir-name-depth 3 --highlight-users --highlight-dirs --stop-at-end -720x400 --key --bloom-intensity 1.1 --hash-seed 11 -o f9-gource.ppm --log-format custom --max-file-lag 1 -
# video creation
# ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i f9-gource.ppm -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 gource.mp4



import csv
import datetime

def csv_open( csv_file ):
	storepath = []
	with open(csv_file, newline = '\n') as csvfile:
		content = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in content:
			if row[1] not in storepath:
				mode = 'A'
				storepath.append(row[1])
			else:
				mode = 'M'
			time = datetime.datetime.strptime( row[2], "%Y-%m-%d %H:%M:%S" )
			timestamp = int( time.timestamp() )
			print( timestamp, '|', row[0], '|', mode, '|', row[1], sep='')


csvf = 'db-2018-03-10.csv'
csv_open( csvf )

