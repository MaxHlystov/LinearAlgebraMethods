## Function solveGaussElimination(n, m, a) solve system of linear equations.
## Theory see at https://en.wikipedia.org/wiki/Gaussian_elimination
## It takes:
##   n - number of equations.
##   m - number of variables.
##   a - matrix: n rows by m+1 columns.
##       Where first m columns represent coefficients of equations,
##       and last (m+1) column are the constant terms.
## Returns tuple (message, result):
##   message - string "YES" - solution was found,
##             "NO" - solution do not exist,
##             "INF" - there are infinit number of solutions.
##   result - if message == "YES" contains values of the variables
##            such that all the equations are simultaneously satisfied.
##
## In Russian.
##Напишите программу, которая решает систему линейных алгебраических
##уравнений методом Гаусса.
##
##Формат входных данных: 
##В первой строке задаются два числа: количество уравнений n
## (n≥1) и количество неизвестных m (m≥1). Далее идут n строк, каждая
##из которых содержит m+1 число. Первые m чисел — это коэффициенты
##i-го уравнения системы, а последнее, (m+1)-е число — коэффициент bi,
##стоящий в правой части i-го уравнения.
##
##Формат выходных данных:
##В первой строке следует вывести слово YES, если решение существует
##и единственно, слово NO в случае, если решение не существует,
##и слово INF в случае, когда решений существует бесконечно много.
##Если решение существует и единственно, то во второй строке следует
##вывести решение системы в виде m чисел, разделенных пробелом.
##
##Sample Input 1:
##
##3 3
##4 2 1 1
##7 8 9 1
##9 1 3 2
##
##Sample Output 1:
##
##YES
##0.2608695652173913 0.04347826086956526 -0.1304347826086957
##
##Sample Input 2:
##
##2 3
##1 3 4 4
##2 1 4 5
##
##Sample Output 2:
##
##INF
##
##Sample Input 3:
##
##3 3
##1 3 2 7
##2 6 4 8
##1 4 3 1
##
##Sample Output 3:
##
##NO


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


def solveGaussElimination(n, m, a):
    """ (int, int, list of list of float) => list of list of float
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


if __name__ == "__main__":

    def findAndPrintSolution(n, m, a):
        print("Matrix ({0} x {1})".format(n, m))
        for row in a:
            print(" ".join(map(str, row)))
            
        message, res = solveGaussElimination(n, m, a)
        print("Solution:", message)
        if message == 'YES':
            print(" ".join(map(str, res)))
        print("")

        
    print("Several examples of the function work:\n")
    
    n, m = 1, 1
    a = [[-7.0, -6.0]]
    findAndPrintSolution(n, m, a)
    
    n, m = 4, 4
    a = [[2, 3, -1, 1, 1],
         [8, 12, -9, 8, 3],
         [4, 6, 3, -2, 3],
         [2, 3, 9, -7, 3]]
    findAndPrintSolution(n, m, a)

    n, m = 1, 3
    a = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    findAndPrintSolution(n, m, a)
    
    n, m = 3, 3
    a = [[4, 2, 1, 1],
         [7, 8, 9, 1],
         [9, 1, 3, 2]]
    findAndPrintSolution(n, m, a)

    n, m = 2, 3
    a = [[1, 3, 4, 4],
         [2, 1, 4, 5]]
    findAndPrintSolution(n, m, a)

    n, m = 3, 3
    a = [[1, 3, 2, 7],
         [2, 6, 4, 8],
         [1, 4, 3, 1]]
    findAndPrintSolution(n, m, a)
