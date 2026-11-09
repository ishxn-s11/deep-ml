import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    # Your code here
    pass
    B=A.T @ A
    
    a=B[0,0]
    b=B[0,1]
    d=B[1,1]
    theta=0.5*np.arctan2(2*b,a-d)
    c=np.cos(theta)
    s=np.sin(theta)
    J=np.array([[c,-s],[s, c]])
    
    D=J.T @ B @ J

    eigenval=np.diag(D)
    eigenval=np.maximum(eigenval,0)
    S=np.sqrt(eigenval)
    idx=np.argsort(S)[::-1]
    S=S[idx]
    V=J[:,idx]
    U=np.zeros((2,2))
    
    for i in range(2):
        
        if S[i]>1e-12:
            U[:,i]=(A @ V[:,i])/S[i]
            
    if S[0]>1e-12 and S[1]<=1e-12:
        U[:,1]=np.array([-U[1,0],U[0,0]])
    elif S[0]<=1e-12:
        U=np.eye(2)
        
    Vt=V.T
    
    return U,S,Vt