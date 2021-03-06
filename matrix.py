import math
import random

def print_matrix( matrix ):
    final = ''
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            final += str(matrix[col][row]) + ' '
        final += '\n'
    print final

def ident( matrix ):
    new_matrix()
    for i in range(0, 4, 1):
        matrix[i][i] = 1

#m1 * m2 -> m2
#matrix syntax: matrix[column#][row#]
def matrix_mult( m1, m2 ):
    final = new_matrix(len(m1[0]), len(m2))
    for col in range(len(m2)):
        for row in range(len(m1[0])):
            temp = 0
            for item in range(len(m1[0])):
                temp += (m1[item][row] * m2[col][item])
            final[col][row] = temp
    for row in range(len(m2[0])):
        for col in range(len(m2)):
            m2[col][row] = final[col][row]

def random_matrix(matrix):
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            matrix[col][row] = random.randint(0,9)

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
