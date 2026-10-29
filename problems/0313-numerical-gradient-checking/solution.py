import numpy as np

def numerical_gradient_check(f, x, analytical_grad, epsilon=1e-7):
    """
    Perform numerical gradient checking using centered finite differences.
    
    Args:
        f: A function that takes a numpy array and returns a scalar
        x: numpy array, the point at which to check gradient
        analytical_grad: numpy array, the analytically computed gradient
        epsilon: float, small value for finite difference approximation
    
    Returns:
        tuple: (numerical_grad, relative_error)
    """
    # Your code here
    pass

    x=np.asarray(x,dtype=float)
    analytical_grad=np.asarray(analytical_grad,dtype=float)
    num_grad=np.zeros_like(x)

    for i in range(x.size):
        x_plus=x.copy()
        x_minus=x.copy()
        x_plus.flat[i]+=epsilon
        x_minus.flat[i]-=epsilon
        num_grad.flat[i]=(f(x_plus)-f(x_minus))/(2*epsilon)

    num_norm=np.linalg.norm(num_grad)
    anlyt_norm=np.linalg.norm(analytical_grad)
    den=num_norm+anlyt_norm

    if den==0:
        relerror=0.0
    else:
        relerror=(np.linalg.norm(num_grad-analytical_grad)/den)

    return num_grad,relerror
