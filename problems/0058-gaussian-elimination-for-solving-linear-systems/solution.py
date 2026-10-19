import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.

    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """

    A=np.array(A,dtype=float,copy=True)
    b=np.array(b,dtype=float,copy=True)
    n=len(b)

    #Forward Elimination

    for k in range(n):
        pivot=k+np.argmax(np.abs(A[k:,k]))

        if abs(A[pivot,k])<1e-12:
            raise ValueError("Matrix is singular")

        A[[k,pivot]]=A[[pivot,k]]
        b[[k,pivot]]=b[[pivot,k]]

        for i in range(k+1,n):
            f=A[i,k]/A[k,k]
            A[i,k:]-=f*A[k,k:]
            b[i]-=f*b[k]

    #Backward Substitution
    x=np.zeros(n)

    for i in range(n-1,-1,-1):
        total=np.dot(A[i,i+1:],x[i+1:])
        x[i]=(b[i]-total)/A[i,i]

    return x
