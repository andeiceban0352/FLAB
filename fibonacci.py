import time
import math
import matplotlib.pyplot as plt

#Algoritmul recursiv
def fib1(n):
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

#Algoritmul iterativ
def fib2(n):
    a = 0
    b = 1
    if n < 0:
        print("Enter a number greater than 0")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b

#Dynamic programing
def fib3(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]
    print(fibonacci(9))



#Power
def multiply(X, Y):
    M = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                M[i][j] += X[i][k] * Y[k][j]
    return M

def fib4(X, n):
    if n <= 1:
        return X
    else:
        Y = fib4(X, n//2)
        M = multiply(Y, Y)
        if n % 2 == 0:
            return M
        else:
            return multiply(M, X)

#fib5 Matrix
def fib5(n):
    if n<=1:
        return n
    else:
        X = [[1, 1], [1, 0]]
        M = fib4(X, n-1)
        return M[0][0]

#Recurrence matrix
def fib6(n):
    if n<=1:
        return n
    else:
        X = [[1, 1], [1, 0]]
        M = multiply(X, [[1, 1], [1, 0]])
        for i in range(2, n):
            M = multiply(M, X)
        return M[0][0]

#Closed form
def fib7(n):
    g = (1 + 5 ** .5) / 2 #golden ratio
    return int(round((g ** n - (1 - g) ** n) / 5 ** .5))