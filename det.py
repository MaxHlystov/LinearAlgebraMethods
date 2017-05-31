# Functin det() compute a determinant of a square matrix
#
# Функция det() вычисляет детерминант квадратной матрицы


def findNotZeroIndex(a, fromIdx):
    """ ([[int]], int) => int
        Look up not zero item from a[fromIdx][fromIdx]
        to a[len(a)][fromIdx].
        if found return index
        if did not find return -1
    """
    n = len(a)
    for i in range(fromIdx+1,n):
        if a[i][fromIdx] != 0:
            return i
    return -1


def makeDiagonalMatrix(a):
    """ ([n, n]) => (int, [n, n])
        Make matrix with zeros below the main diagonal.
        n = len(a) == len(a[0]).
        Return tuple of sign of diagonal matrix and
        the matrix.
        Sign is (-1)^(count of rows swap)
    """
    sign = 1
    n = len(a)
    for i in range(n):
        startCol = i
        while startCol < n and a[i][startCol] == 0:
            # try to find not zero factor, and swap
            # with current row
            notZeroIdx = findNotZeroIndex(a, i)
            if notZeroIdx != -1:
                # swap two rows
                a[i], a[notZeroIdx] = a[notZeroIdx], a[i]
                sign *= -1
                break
            # all rows with zero factors
            # step to the right to find column without zeros
            startCol += 1

        if startCol == n:
            return (sign, a)
        
        ai = a[i]
        for j in range(i+1, n):
            aj = a[j]
            k = aj[startCol] / ai[startCol]
            for idx in range(startCol, n):
                aj[idx] -= k * ai[idx]
            a[j][i] = 0
            
    return (sign, a)


def det(a):
    """ ([[]]) => float
        Compute a determinant of a square matrix. """
    n = len(a)
    if n == 1:
        return a[0][0]
    res = 1
    sig, diagMatrix = makeDiagonalMatrix(a)
    for i in range(n):
        res *= a[i][i]
    return res*sig


if __name__ == "__main__":
    a = [[4, 2],
         [5, 3]]
    n = len(a)

    print("For matrix {} x {}".format(n,n))
    for row in a:
        print(" ".join(map(str, row)))
    print("Determinant is", ('%f' % det(a)).rstrip('0').rstrip('.'))
    print("")
    
    a = [[4, 2, 8],
         [5, 2, 4],
         [2, 6, 2]]
    n = len(a)
    
    print("For matrix {} x {}".format(n,n))
    for row in a:
        print(" ".join(map(str, row)))
    print("Determinant is", ('%f' % det(a)).rstrip('0').rstrip('.'))
