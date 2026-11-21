import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    pass

    X=np.array(X,dtype=float)
    norms=np.linalg.norm(X,axis=1,keepdims=True)
    norms[norms==0]=1
    xnorm=X/norms
    s=xnorm @ xnorm.T

    return np.round(s,4).tolist()