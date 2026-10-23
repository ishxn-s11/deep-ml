import numpy as np
import math

def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	pass
	
	if func_name=="poly2d":
		x,y=point
		dx=2*x*y+y**2
		dy=x**2+2*x*y
		
		return (float(dx),float(dy))
		
	elif func_name=="exp_sum":
		x,y=point
		dx=math.exp(x+y)
		dy=math.exp(x+y)
		
		return (float(dx),float(dy))
		
	elif func_name=="product_sin":
		x,y=point
		dx=math.sin(y)
		dy=x*math.cos(y)
		
		return (float(dx),float(dy))
	
	elif func_name=="poly3d":
		x,y,z=point
		dx=2*x*y
		dy=x**2+z**2
		dz=2*y*z
		
		return (float(dx),float(dy),float(dz))
		
	elif func_name=="squared_error":
		x,y=point
		dx=2*(x-y)
		dy=-2*(x-y)
		
		return (float(dx),float(dy))
		
	else:
		
		raise ValueError("Unknown function name")