# Based on http://en.wikipedia.org/wiki/Information_retrieval
# Reference code:
# https://gist.github.com/ajschumacher/2891017
# https://github.com/benhamner/Metrics/blob/master/Python/ml_metrics/average_precision.py
# https://github.com/benhamner/Metrics/blob/master/Python/ml_metrics/test/test_average_precision.py

import csv
import numpy as np

def apk(actual, predicted, k):
	if len(predicted)>k:
		predicted = predicted[:k]

	score = 0.0
	num_hits = 0.0

	for i,p in enumerate(predicted):
		if p in actual and p not in predicted[:i]:
			num_hits += 1.0
			score += num_hits / (i+1.0)

	if not actual:
		return 1.0

	return score / min(len(actual), k)

def mapk(actual, predicted):
	k=50
	return np.mean([apk(a,p,k) for a,p in zip(actual, predicted)])


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
		reader.next()
		for line in reader:
			(UserID, applications)=line
			pops[UserID]=[]
			apps_split=applications.split(" ")
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
		if i in p_key:
			a.append(apps[i])
			p.append(pops[i])
	baseResult=mapk(a,p)		
	print baseResult



Compare()	
