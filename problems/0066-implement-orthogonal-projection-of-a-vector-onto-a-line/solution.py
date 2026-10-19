import  numpy as np

def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	pass

	numr=sum(np.dot(v[i],L[i]) for i in range(len(v)))
	denr=sum(L[i]**2 for i in range(len(L)))

	if denr==0:

		raise ValueError("Cannot project onto a zero vector")
	
	scl=numr/denr
	res=[round(scl*x) for x in L]

	return res
