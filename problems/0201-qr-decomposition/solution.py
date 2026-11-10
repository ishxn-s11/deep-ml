import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """
    Perform QR decomposition using Gram-Schmidt process.
    
    Args:
        A: An m x n matrix represented as list of lists
    
    Returns:
        Tuple of (Q, R) where Q is orthogonal and R is upper triangular
    """
    # Your code here
    pass

    A=np.array(A,dtype=float)
    m,n=A.shape
    Q=np.zeros((m,n))
    R=np.zeros((n,n))

    for i in range(n):
        v=A[:,i].copy()

        for j in range(i):
            R[j,i]=np.dot(Q[:,j],A[:,i])
            v-=R[j,i]*Q[:,j]
        
        R[i,i]=np.linalg.norm(v)

        if np.isclose(R[i,i],0):

            raise ValueError("Columns must be linearly independent")
        
        Q[:,i]=v/R[i,i]
    
    return Q,R