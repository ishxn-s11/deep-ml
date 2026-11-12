import numpy as np

def check_positive_definite(matrix: list) -> dict:
    """
    Check if a matrix is positive definite and compute its eigenvalues.
    
    Args:
        matrix: A 2D list representing a square matrix
        
    Returns:
        dict with 'is_positive_definite' (bool) and 'eigenvalues' (list of floats sorted ascending)
    """
    # Your code here
    pass
    
    A=np.array(matrix,dtype=float)
    is_symm=np.allclose(A,A.T)
    eigenval=np.linalg.eigvals(A)
    eigenval=np.sort(eigenval.real)
    is_posdef=(is_symm and np.all(eigenval>1e-10))
    
    return {
        'is_positive_definite':bool(is_posdef),
        'eigenvalues':np.round(eigenval,4).tolist()
    }