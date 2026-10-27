import numpy as np

def cross_entropy_derivative(logits: list[float], target: int) -> list[float]:
	"""
	Compute the derivative of cross-entropy loss with respect to logits.
	
	Args:
		logits: Raw model outputs (before softmax)
		target: Index of the true class (0-indexed)
		
	Returns:
		Gradient vector where gradient[i] = dL/d(logits[i])
	"""
	# Your code here
	pass
	
	logits=np.array(logits, dtype=float)
	exp_logt=np.exp(logits-np.max(logits))
	prob=exp_logt/np.sum(exp_logt)
	prob[target]-=1
	
	return prob