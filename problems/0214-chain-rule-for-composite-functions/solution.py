import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# Your code here
	pass
	val=x
	d=1.0
	
	for func in reversed(functions):
		
		if func=='square':
			d*=2*val
			val=val**2
		
		elif func=='sin':
			d*=np.cos(val)
			val=np.sin(val)

		elif func=='exp':
			val=np.exp(val)
			d*=val
			
		elif func=='log':
			d/=val
			val=np.log(val)
			
	return d