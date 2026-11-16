import numpy as np

def multivariate_kl_divergence(mu_p: np.ndarray, Cov_p: np.ndarray, mu_q: np.ndarray, Cov_q: np.ndarray) -> float:
    """
    Computes the KL divergence between two multivariate Gaussian distributions.
    
    Parameters:
    mu_p: mean vector of the first distribution
    Cov_p: covariance matrix of the first distribution
    mu_q: mean vector of the second distribution
    Cov_q: covariance matrix of the second distribution

    Returns:
    KL divergence as a float
    """
    # Your code here
    pass

    k=len(mu_p)
    t1=np.log(np.linalg.det(Cov_q)/np.linalg.det(Cov_p))
    d=mu_p-mu_q
    t2=d.T @ np.linalg.inv(Cov_q) @ d
    t3=np.trace(np.linalg.inv(Cov_q) @ Cov_p)

    return float(0.5*(t1+t2+t3-k))