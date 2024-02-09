# Do NOT use any external libraries

def solve(A, b):
    """A is a m x n matrix, and b is an n x 1 vector.
    returns: x, where x is the solution to the equation Ax = b
    if no solution exists, return -1
    if infinite solutions exist, return -2"""
    n = len(A)
        for i in range(n):
            if A[i][i] == 0:
                return -1
            for j in range(n):
                if i != j:
                    ans = A[j][i]/A[i][i]
                    for k in range(n):
                        A[j][k] = A[j][k] - ans * A[i][k]
                    B[j] = B[j] - ans * B[i]
        for i in range(n):
            if A[i][i] == 0:
                return -1
            B[i] = B[i]/A[i][i]
            A[i][i] = 1
        return B
    return gauss(A, B)


def det(A):
    """calculates the determinant of A
    if A is not a square matrix, return 0"""
    if len(A) != len(A[0]):
        return 0
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        det = 0
        for i in range(len(A)):
            det += ((-1)**i)*A[0][i]*det(minor(A, 0, i))
        return det
        
def minor(i, j, k):
    return [row[:k] + row[k+1:] for row in (i[:k]+i[j+1:])]
    
