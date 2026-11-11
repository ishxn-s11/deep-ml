import numpy as np

def lu_decomposition(A: list) -> tuple:
    """
    Perform LU decomposition on a square matrix using Doolittle's method.
    
    Args:
        A: Square matrix as a list of lists
    
    Returns:
        U is upper triangular, and A = L @ U
    """
    # Your code here
    pass

    A=np.array(A,dtype=float)
    n=A.shape[0]
    L=np.eye(n)
    U=np.zeros((n,n))

    for i in range(n):

        for j in range(i,n):
            sum1=0

            for k in range(i):
                sum1+=L[i,k]*U[k,j]
            
            U[i,j]=A[i,j]-sum1
        
        for j in range(i+1,n):
            sum2=0

            for k in range(i):
                sum2+=L[j,k]*U[k,i]
            
            L[j,i]=(A[j,i]-sum2)/U[i,i]
    
    return L,U
