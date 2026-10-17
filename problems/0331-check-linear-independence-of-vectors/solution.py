import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    pass

    if not vectors:

        return True

    rows=len(vectors)
    cols=len(vectors[0])

    if rows>cols:

        return False

    A=[row[:] for row in vectors]
    rank=0
    tol=1e-10

    for col in range(cols):
        pivot=max(range(rank,rows),key=lambda r:abs(A[r][col]))

        if abs(A[pivot][col])<tol:
            continue

        A[rank],A[pivot]=A[pivot],A[rank]

        for r in range(rank+1,rows):
            f=A[r][col]/A[rank][col]

            for c in range(col,cols):
                A[r][c]-= f*A[rank][c]

        rank+=1

        if rank==rows:

            break

    return rank==rows