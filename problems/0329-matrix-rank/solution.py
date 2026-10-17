import numpy as np

'''
Create A Copy 
Initialise rank=0
Iterate Via Each Column 
Select The Pivot => The Row With The Largest Absolute Pivot
Check The Tolerance 
Swap Rows 
Eliminate Rows Using factor=A[i][col]/A[rank][col]

Time Complexity: O(m*n*min(m,n))
Space Complexity: O(m*n)
'''

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    # Your code here
    pass

    A=A.astype(float).copy()
    m,n=A.shape
    rank=0

    for col in range(n):

        if rank==m:

            break
        
        pvt=rank+np.argmax(np.abs(A[rank:,col]))

        if abs(A[pvt,col])<=tol:
            
            continue
        
        A[[rank,pvt]]=A[[pvt,rank]]

        for i in range(rank+1,m):
            f=A[i,col]/A[rank,col]
            A[i,:]-=f*A[rank,:]
        
        rank+=1

    return rank
        
