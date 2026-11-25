import numpy as np

def rref(A):
    # Your code here
    pass

    A=np.array(A,dtype=float)
    r,c=A.shape
    pivot_row=0
    for i in range(c):
        pivot=pivot_row

        while pivot<r and abs(A[pivot,i])<1e-10:
            pivot+=1
        
        if pivot==r:
            continue
        
        A[[pivot_row,pivot]]=A[[pivot,pivot_row]]
        A[pivot_row]/=A[pivot_row,i]

        for j in range(r):

            if j!=pivot_row:
                factor=A[j,i]
                A[j]-=factor*A[pivot_row]
        
        pivot_row+=1

        if pivot_row==r:
            break
    
    A[np.abs(A)<1e-10]=0

    return A
