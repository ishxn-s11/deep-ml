import numpy as np

def cramers_rule(A, b):
    # Your code here
    pass

    A=np.array(A,dtype=float)
    b=np.array(b,dtype=float)
    detA=np.linalg.det(A)
    
    if np.isclose(detA,0):

        return -1
    
    n=len(b)
    x=np.zeros(n)

    for i in range(n):
        temp=A.copy()
        temp[:,i]=b
        x[i]=np.linalg.det(temp)/detA

    return x