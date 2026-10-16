def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    n=len(matrix)
    tr=sum(matrix[i][i] for i in range(n))

    def det(mat):
        size=len(mat)

        if size==1:

            return mat[0][0]

        if size==2:

            return(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])

        res=0

        for j in range(size):
            m=[row[:j]+row[j+1:] for row in mat[1:]]
            res+=(-1)**j*mat[0][j]*det(m)

        return res

    return (float(det(matrix)),float(tr))