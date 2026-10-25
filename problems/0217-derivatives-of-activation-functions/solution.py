import numpy as np

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	# Your code here
	pass
	
	sigmoid=1/(1+np.exp(-x))
	tanh=np.tanh(x)
	
	return {
		'sigmoid':sigmoid*(1-sigmoid),
		'tanh':1-tanh**2,
		'relu':np.maximum(0,np.sign(x)) if x>0 else 0.0
    }