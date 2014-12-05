import sys
from sets import Set

users = Set()
f = open('cleaned_Train_apps.csv')
for line in f:
	l = line.rstrip().split(',')
	if l[0] not in users:
		users.add(l[0])

inFileName = sys.argv[1]
outFileName1 = 'cleaned_Train_' + inFileName + '.csv'
outFileName2 = 'cleaned_Test_' + inFileName + '.csv'

inFile = open(inFileName + '.tsv')
outFile1 = open(outFileName1, 'w')
outFile2 = open(outFileName2, 'w')

header = inFile.readline()
hl = header.rstrip().split()
# UserID,City,State,Country,DegreeType,Major,WorkHistoryCount,TotalYearsExperience,CurrentlyEmployed
new_index = [0, 3, 4, 5, 7, 8, 10, 11, 12]
new_header = ''
for i in new_index:
	new_header = new_header + hl[i] + ','
new_header = new_header[:-1] + '\n' 
outFile1.write(new_header)
outFile2.write(new_header)

def clean(s):
	char = [',', '(', '[', '{']
	for c in char:
		index = s.find(c)
		if index != -1:
			s = s[:index]
	return s

s = Set()
count = 0
# err = 0

for line in inFile:
	# count += 1
	# print  "count: " + str(count)
	try:
		line.encode('ascii')
	except UnicodeDecodeError:
		# err += 1
		# print "err: " + str(err)
		continue
	t = Set(line)
	if count < 10000:
		# print "count: " + str(count)
		s = s.union(t)
	else:
		if not t <= s:
			continue
	l = line.rstrip().split('\t')
	new = ''
	for i in new_index:
		if l[i] == '':
			if i == 8:
				l[i] = 'None'
			elif i == 10:
				l[i] = '0'
			elif i == 11:
				l[i] = '0'
			elif i == 12:
				l[i] = 'No'
		new += clean(l[i]) + ','
	new = new[:-1] + '\n'
	# if not Set(new) <= alphabet:
	# 	continue
	if l[2] == 'Test':
		outFile2.write(new)
	# if l[0] not in users:
	# 	continue
	if l[2] == 'Train':
		outFile1.write(new)