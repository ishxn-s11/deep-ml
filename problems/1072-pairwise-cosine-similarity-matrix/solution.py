import numpy as np

def pairwise_cosine_similarity(X):
    # Your code here
    pass

    n=len(X)
    res=[[0.0]*n for i in range(n)]

    for i in range(n):

        for j in range(n):
            dot=sum(X[i][k]*X[j][k] for k in range(len(X[i])))
            norm_i=np.sqrt(sum(x*x for x in X[i]))
            norm_j=np.sqrt(sum(x*x for x in X[j]))

            if norm_i==0 or norm_j==0:
                sim=0.0
            else:
                sim=dot/(norm_i*norm_j)
            
            res[i][j]=round(sim,4)
    
    return res