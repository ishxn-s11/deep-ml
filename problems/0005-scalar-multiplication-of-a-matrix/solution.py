def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here

	res=[]

	for i in matrix:
		nr=[]

		for j in i: 
			nr.append(j*scalar)
		
		res.append(nr)

	return res

	pass