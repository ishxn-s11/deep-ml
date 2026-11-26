import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
    A=np.array(A,dtype=float)
    b=np.array(b,dtype=float)

    if x_ini is None:
        x=np.zeros(len(b))
    else:
        x=np.array(x_ini,dtype=float)

    for _ in range(n):

        for i in range(len(b)):
            s=0

            for j in range(len(b)):
                if i!=j:
                    s+=A[i][j]*x[j]

            x[i]=(b[i]-s)/A[i][i]

    return x
