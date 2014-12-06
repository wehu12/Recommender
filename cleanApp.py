import sys

inFileName = sys.argv[1]
outFileName1 = 'cleaned_Train_' + inFileName + '.csv'
outFileName2 = 'cleaned_Test_' + inFileName + '.csv'

inFile = open(inFileName + '.tsv')
outFile1 = open(outFileName1, 'w')
outFile2 = open(outFileName2, 'w')

outFile1.write('UserID,JobID\n')
outFile2.write('UserID,JobID\n')

for line in inFile:
	l = line.split()
	new = l[0] + ',' + l[-1] + '\n'
	if l[2] == 'Train':
		outFile1.write(new)
	elif l[2] == 'Test':
		outFile2.write(new)