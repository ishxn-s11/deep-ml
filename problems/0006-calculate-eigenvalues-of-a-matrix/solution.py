import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a,b=matrix[0]
	c,d=matrix[1]
	tr=a+d
	det=a*d-b*c
	d=tr**2-4*det
	lambda1=(tr+math.sqrt(d))/2
	lambda2=(tr-math.sqrt(d))/2
	
	return sorted([lambda1,lambda2],reverse=True)