import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here

	x=np.array(features,dtype=float)
	y=np.array(labels,dtype=float)
	w=np.array(initial_weights,dtype=float)
	b=float(initial_bias)
	n=len(y)
	mse_val=[]

	for _ in range(epochs):
		z=x @ w+b
		pred=1/(1+np.exp(-z)) #Forward Pass
		mse=np.mean((pred-y)**2)
		mse_val.append(mse) #Storing MSE Values Before Updation
		delta=(2*(pred-y)*pred*(1-pred))
		dw=(x.T @ delta)/n
		db=np.mean(delta)

		w-=learning_rate*dw
		b-=learning_rate*db #Parameter Updation

	return (np.round(w,4).tolist(),round(b,4),
	np.round(mse_val,4).tolist())


