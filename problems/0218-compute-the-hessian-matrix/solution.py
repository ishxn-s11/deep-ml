from typing import Callable

def compute_hessian(f: Callable[[list[float]], float], point: list[float], h: float = 1e-5) -> list[list[float]]:
    """
    Compute the Hessian matrix of function f at the given point using finite differences.
    
    Args:
        f: A scalar function that takes a list of floats and returns a float
        point: The point at which to compute the Hessian (list of coordinates)
        h: Step size for finite differences (default: 1e-5)
        
    Returns:
        The Hessian matrix as a list of lists (n x n where n = len(point))
    """
    # Your code here
    pass

    n = len(point)
    h = 1e-5

    H = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if i == j:
                x1 = point.copy()
                x2 = point.copy()

                x1[i] += h
                x2[i] -= h

                H[i][j] = (
                    f(x1) - 2 * f(point) + f(x2)
                ) / (h * h)

            else:
                x1 = point.copy()
                x2 = point.copy()
                x3 = point.copy()
                x4 = point.copy()

                x1[i] += h
                x1[j] += h

                x2[i] += h
                x2[j] -= h

                x3[i] -= h
                x3[j] += h

                x4[i] -= h
                x4[j] -= h

                H[i][j] = (
                    f(x1) - f(x2) - f(x3) + f(x4)
                ) / (4 * h * h)

    return H