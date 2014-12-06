from stripHTML import strip_tags
wd = "/Users/sevensevens/CSE6242_Proj/data/"
f = open(wd + 'cleaned_jobs.csv')
ids = [1050736, 1078744, 779460, 317343, 152528, 757625, 553828]
header = f.readline()
print new_header
for line in f:
	l = line.rstrip().split(',')
	if int(l[0]) in ids:
		new = ','.join(l)
		print new
