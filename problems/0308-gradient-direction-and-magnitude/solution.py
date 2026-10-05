import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	pass

	mag=sum(x**2 for x in gradient)**0.5

	if mag==0:
		direction=[0.0 for _ in gradient]
		descent_dir=[0.0 for _ in gradient]
	else:
		direction=[x/mag for x in gradient]
		descent_dir=[-x for x in direction]

	return {"magnitude":float(mag),"direction":direction,"descent_direction":descent_dir}