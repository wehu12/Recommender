import sys
from sets import Set 
import string

jobs = Set()
f = open('cleaned_Train_apps.csv')
for line in f:
	l = line.rstrip().split(',')
	if l[1] not in jobs:
		jobs.add(l[1])

inFileName = sys.argv[1]
outFileName = 'cleaned_' + inFileName + '.csv'

inFile = open(inFileName + '.tsv')
outFile = open(outFileName, 'w')

header = inFile.readline()
hl = header.rstrip().split()
# JobID,Title,City,State,Country
new_index = [0, 2, 5, 6, 7]
new_header = ''
for i in new_index:
	new_header = new_header + hl[i] + ','
new_header = new_header[:-1] + '\n'
outFile.write(new_header)

def clean(s):
	char = [',', '(', '[', '{']
	for c in char:
		index = s.find(c)
		if index != -1:
			s = s[:index]
	return s

s = Set()
count = 0
err = 0

for line in inFile:
	count += 1
	# print count

	t = Set(line)
	if count < 1000000:
		s = s.union(t)
	else:
		if not t <= s:
			continue
	l = line.rstrip().split('\t')
	if l[0] not in jobs:
		continue
	new = ''
	for i in new_index:
		new += clean(l[i]) + ','
	new = new[:-1] + '\n'
	new = filter(lambda x: x in string.printable, new)
	try:
		new.encode('ascii')
	except UnicodeDecodeError:
		err += 1 
		print new
		continue
	if "'" in new or '"' in new:
		continue
	outFile.write(new)