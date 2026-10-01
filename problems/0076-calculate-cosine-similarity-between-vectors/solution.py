import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	if v1.shape!=v2.shape:
		raise ValueError("Vectors must have the same shape")
	
	if v1.size==0:
		raise ValueError("Vector cannot be empty")
	
	v1_norm=np.linalg.norm(v1)
	v2_norm=np.linalg.norm(v2)

	if v1_norm==0 or v2_norm==0:
		raise ValueError("Vectors cannot have zero magnitude")

	sim=np.dot(v1,v2)/(v1_norm*v2_norm)

	return float(sim) 
	pass