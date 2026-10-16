def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    res=[]

    if mode=="row":

        for i in matrix:
            mean=sum(i)/len(i)
            res.append(mean)
    elif mode=="column":

        for i in range(len(matrix[0])):
            total=0

            for j in range(len(matrix)):
                total+=matrix[j][i]

            mean=total/len(matrix)
            res.append(mean)

    return res