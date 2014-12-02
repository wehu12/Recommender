import csv
from score import *
def readAppData():
	with open("./data/app_cleaned.csv","r") as af:
		reader = csv.reader(af, delimiter=",",
			quoting=csv.QUOTE_NONE, quotechar="")
		apps=dict()
		i=0
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
		i=0
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
	a=[]; p=[]
	for app in apps:
		for pop in pops:
			if app == pops:
				a.append(apps[app])
				p.append(pops[pop])
	result=mapk(a,p)			
	print result

Compare()	
