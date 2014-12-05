from sets import Set  

users = dict()
wd = "/Users/sevensevens/CSE6242_Proj/data/"
f = open(wd + 'popular_jobs.csv')
for line in f:
	l = line.rstrip().split(',')
	userID, jobs = l[0], l[1]
	if userID not in users:
		users[userID] = jobs.split()

f.close()
features = 'All'
f = open('rf_' + features + '_result.csv')
f2 = open('combine_' + features + '_tmp_result.csv', 'w')
for line in f:
	l = line.rstrip().split(',')
	userID, jobs = l[0], l[1]
	if userID not in users:
		continue
	new_jobs = [job for job in jobs.split() if job in users[userID]]
	newline = userID + ',' + ' '.join(new_jobs) + '\n'
	f2.write(newline)
