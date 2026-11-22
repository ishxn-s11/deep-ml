import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    
    r,c=new_shape
    m=len(a)
    n=len(a[0]) if m>0 else 0

    if m*n!=r*c:

        return []
    
    arr=[]

    for i in a:

        for j in i:
            arr.append(j)
    
    res=[]

    for i in range(r):
        start=i*c
        end=(i+1)*c
        res.append(arr[start:end])

    return res