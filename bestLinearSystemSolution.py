## Function findBestSolution(n, m, a) finds the best fit solution
## for the system of linear equation where the number of equation
## is bigger than the number of variables.
## It minimise sqared error between vector of constant terms b and
## computed by the system values.
## For example, we have some linear model Y=C*X.
## Where Y - vector of outputs (size n*1);
##  X - vector of inputs (size n*m);
##  C - vector of coefficients (size m).
## If we want to find coefficients, which will give the best output
## by given input vector x (m - count of inputs), we need to make
## a lot of measurements (size n). And we will take two vectors
## X (inputs) and Y (mesured outputs). One row of the vectors
## is a measure. Then we found by findBestSolution() function vector
## of coefficients, that best predicts outputs y by any x vector
## of inputs.
##
## In Russian.
##Напишите программу, которая находит наилучшее решение системы
##линейных алгебраических уравнений методом наименьших квадратов.
##
##Формат входных данных:
##В первой строке задаются два числа: количество уравнений
##n и количество неизвестных m. Количество уравнений не меньше
##количества неизвестных. Далее идут n строк, каждая из которых
##содержит m+1 число. Первые m чисел - это коэффициенты
##i-го уравнения системы, а последнее, (m+1)-е число - коэффициент
##bi, стоящий в правой части i-го уравнения.
##
##Формат выходных данных:
##В качестве результата следует вывести решение системы в виде
##m чисел, разделенных пробелом.
##
##Sample Input:
##4 2
##4 2 8 
##5 2 4 
##2 6 2 
##3 0 8 
##
##Sample Output:
##1.6531165311653115 -0.30894308943089427


def isZeroRow(m, row):
    """ (int, [m]) => boolean
      check if row with length m consists of only zeros
    """
    for i in range(m):
        if row[i] != 0:
            return False
    return True


def findNotZeroIndex(n, a, fromIdx):
    """ (int, [[int]]) => int
        find not zero item from a[fromIdx][fromIdx]
        to a[len(a)][fromIdx]
        if found return index
        if did not find return -1
    """
    n = len(a)
    for i in range(fromIdx+1,n):
        if a[i][fromIdx] != 0:
            return i
    return -1


def makeDiagonalMatrix(n, m, a):
    """ (int, int, [n, m]) => [n, m]
        Make matrix with zeros below the main diagonal.
    """
    for i in range(min(n, m)):
        startCol = i
        while startCol < m and a[i][startCol] == 0:
            # try to find not zero factor, and swap
            # with current row
            notZeroIdx = findNotZeroIndex(n, a, i)
            if notZeroIdx != -1:
                # swap two rows
                a[i], a[notZeroIdx] = a[notZeroIdx], a[i]
                break
            # all rows with zero factors
            # step to the right to find column without zeros
            startCol += 1

        if startCol == m:
            return a
        
        ai = a[i]
        for j in range(i+1, n):
            aj = a[j]
            k = aj[startCol] / ai[startCol]
            for idx in range(startCol, m+1):
                aj[idx] -= k * ai[idx]
            a[j][i] = 0
    return a


def solveGauss(n, m, a):
    """    
        find solve of the linear system of equations
        by Gauss way.
        Return tuple:
        first - string:
         "YES" - there is a solution;
         "NO" - there is not a solution;
         "INF" - infinit number of solutions.
        second - list:
         if first is "YES", then contains roots;
         else it is None
    """ 
    if n == 0 or m == 0:
        return ("NO", None)
    if n == 1 and m == 1:
        if a[0][0] == 0:
            return ("NO", None)
        return ("YES", [a[0][1]/a[0][0]])
    
    makeDiagonalMatrix(n, m, a)
    #print(a)
    rowsIndicesToDelete = []
    for i in range(n):
        if isZeroRow(m, a[i]):
            if a[i][m] == 0:
                # we need to remove this row
                rowsIndicesToDelete.append(a[i])
            else:
                # there are not an equation solution
                return ("NO", None)
    if rowsIndicesToDelete:
        for row in rowsIndicesToDelete:
            del row
        n -= len(rowsIndicesToDelete)
    if n < m:
        return ("INF", None)
    
    res = [0] * m
    for i in range(n-1,-1,-1):
        # compute x_i
        if a[i][i] == 0:
            raise Exception("ZERO" + str(i), a)
        
        res[i] = a[i][m] / a[i][i]
        # change equation above by substract x_i from b
        for j in range(i):
            a[j][m] -= res[i] * a[j][i]
    return ("YES", res)


def findBestSolution(n, m, a):
    """ find solution of linear equation system
        by square error minimisation.
        (int, int, [[float],...[float]]) => [float]
        n - number of rows in a.
        m - number of items in each row in a - 1.
        a - matrix float^(n,m). The last column is
            the b coefficients of equation.
    """
    # new matrix to find projection of the vector y = a[:][m]
    # on the hyperplane a[:][1:m-1].
    e = [[0]*(m+1) for _ in range(m)]
    for rowIdx in range(m):
        # go through the rows in e
        for colIdx in range(m+1):
            # go through the columns in e
            for k in range(n):
                e[rowIdx][colIdx] += a[k][rowIdx] * a[k][colIdx]
    message, res = solveGauss(m, m, e)
    if message == 'YES':
        return res
    return []

        
if __name__ == "__main__":
    n, m = 4, 2
    a = [[4, 2, 8],
         [5, 2, 4],
         [2, 6, 2],
         [3, 0, 8]]

    print("For matrix {0} x {1}".format(n,m))
    for row in a:
        print(" ".join(map(str, row)))
    print("The best fit solution is:")
    res = findBestSolution(n, m, a)
    print(" ".join(map(str, res)))
