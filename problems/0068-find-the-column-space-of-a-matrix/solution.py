
import numpy as np

def matrix_image(A):
    # Write your code here
    pass

    A=np.array(A,dtype=float)
    basis=[]
    curr_rank=0

    for j in range(A.shape[1]):
        col=A[:,j]

        if basis:
            temp=np.column_stack(basis+[col])
        else:
            temp=col.reshape(-1,1)

        new_rank=np.linalg.matrix_rank(temp)

        if new_rank>curr_rank:
            basis.append(col)
            curr_rank=new_rank

    if basis:

        return np.column_stack(basis)

    return np.empty((A.shape[0],0))
