import numpy as np

def entropy_and_cross_entropy(P: list[float], Q: list[float]) -> tuple[float, float]:
    """
    Compute entropy of P and cross-entropy between P and Q.
    
    Args:
        P: True probability distribution
        Q: Predicted probability distribution
    
    Returns:
        Tuple of (entropy H(P), cross-entropy H(P,Q))
    """
    # Your code here
    pass

    P=np.array(P,dtype=float)
    Q=np.array(Q,dtype=float)
    mask=P>0
    entropy=-np.sum(P[mask]*np.log(P[mask]))
    
    if np.any((P>0) & (Q==0)):
        xentropy=float('inf')
    else:
        xentropy=-np.sum(P[mask]*np.log(Q[mask]))
        
    return float(entropy),float(xentropy)