import numpy as np

def calculate_correlation_matrix(X, Y=None):
	# Your code here
	
	X=np.asarray(X)
	
	if Y is None:

		return np.corrcoef(X,rowvar=False)
	
	Y=np.asarray(Y)
	
	return np.corrcoef(X,Y,rowvar=False)[:X.shape[1],X.shape[1]:]