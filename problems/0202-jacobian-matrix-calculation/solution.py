import numpy as np

def jacobian_matrix(f, x: list[float], h: float = 1e-5) -> list[list[float]]:
	"""
	Compute the Jacobian matrix using numerical differentiation.
	
	Args:
		f: Function that takes a list and returns a list
		x: Point at which to evaluate the Jacobian
		h: Step size for finite differences
	
	Returns:
		Jacobian matrix as list of lists
	"""
	# Your code here
	pass
	
	x=np.array(x,dtype=float)
	f_x=np.array(f(x.tolist()),dtype=float)
	m=len(f_x)
	n=len(x)
	J=np.zeros((m,n))
	
	for j in range(n):
		x_per=x.copy()
		x_per[j]+=h
		f_per=np.array(f(x_per.tolist()),dtype=float)
		J[:,j]=(f_per-f_x)/h
		
	return J