import csv
from score import *
def readAppData():
	with open("./data/app_cleaned.csv","r") as af:
		reader = csv.reader(af, delimiter=",",
			quoting=csv.QUOTE_NONE, quotechar="")
		apps=dict()
		for line in reader:
			(UserID, applications)=line
			apps[UserID]=[]
			apps_split=applications.split("\t")
			for ins in apps_split:
				apps[UserID].append(ins)
	return apps	

def readPopularData():
	with open("./data/popular_jobs.csv","r") as pf:
		reader = csv.reader(pf, delimiter=",",
			quoting=csv.QUOTE_NONE, quotechar="")
		pops=dict()
		for line in reader:
			(UserID, applications)=line
			pops[UserID]=[]
			apps_split=applications.split("\t")
			for ins in apps_split:
				pops[UserID].append(ins)
	return pops			

def Compare():
	apps=readAppData()
	pops=readPopularData()
	a_key=apps.keys()
	p_key=pops.keys()
	a=[]; p=[]
	count=0
	for i in a_key:
		for j in p_key:
			if i==j:
				count+=1
				a.append(apps[i])
				p.append(pops[j])
	print count
	print len(a)	
	print len(b)


Compare()	
