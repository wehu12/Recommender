# Based on http://en.wikipedia.org/wiki/Information_retrieval
# Reference code:
# https://gist.github.com/ajschumacher/2891017
# https://github.com/benhamner/Metrics/blob/master/Python/ml_metrics/average_precision.py
# https://github.com/benhamner/Metrics/blob/master/Python/ml_metrics/test/test_average_precision.py


import numpy as np

def apk(actual, predicted, k=10):
	"""
	Computes the average precision at k.

	This function computes the average prescision at k between two lists of
	items.

	Parameters
	----------
	actual : list
			 A list of elements that are to be predicted (order doesn't matter)
	predicted : list
				A list of predicted elements (order does matter)
	k : int, optional
		The maximum number of predicted elements

	Returns
	-------
	score : double
			The average precision at k over the input lists

	"""
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
	k=10
	"""
	Computes the mean average precision at k.

	This function computes the mean average prescision at k between two lists
	of lists of items.

	Parameters
	----------
	actual : list
	         A list of lists of elements that are to be predicted 
	         (order doesn't matter in the lists)
	predicted : list
	            A list of lists of predicted elements
	            (order matters in the lists)
	k : int, optional
	    The maximum number of predicted elements

	Returns
	-------
	score : double
	        The mean average precision at k over the input lists

	"""
	return np.mean([apk(a,p,k) for a,p in zip(actual, predicted)])


# def test():
# 	correct=[[1,2,3],[2,2,2]]
# 	predicted=[[3,2,6,7],[2,2,2]]
# 	result=mapk(correct,predicted)
# 	print result

# test()	
