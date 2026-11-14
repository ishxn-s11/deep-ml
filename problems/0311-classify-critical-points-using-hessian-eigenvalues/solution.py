import numpy as np

def classify_critical_point(hessian: np.ndarray, tol: float = 1e-10):
    pass
    
    eigenval=np.linalg.eigvalsh(hessian)
    
    if np.any(np.abs(eigenval)<tol):
        
        return None
        
    if np.all(eigenval>0):
        
        return -1
        
    if np.all(eigenval<0):
        
        return 1
        
    return 0