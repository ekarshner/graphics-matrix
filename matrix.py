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
#len(m1[0]) = number of rows, m1 ALSO number of cols, m2
#len(m1) = number of cols, m1
#rownum = row number of pointer, m1
#rowitem = item in row of pointer (essentially col#), m1
#colitem = item in col of pointer (essentially row#), m2
#matrix syntax: matrix[column#][row#]
def matrix_mult( m1, m2 ):
    final = new_matrix(len(m1[0]), len(m2))
    print_matrix(final)
    for rownum in range(len(m1[0])):
        print('rownum')
        print rownum
        for rowitem in range(len(m1)):
            print('rowitem')
            print rowitem
            temp = 0
            for colitem in range(len(m1[0])):
                temp += (m1[rowitem][rownum] * m2[rownum][colitem])
                print('temp')
                print temp
            final[rowitem][rownum] = temp
    m2 = final

def random_matrix(matrix):
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            matrix[col][row] = random.randint(0,10)

def matrix_ordered(matrix):
    i = 0
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            matrix[col][row] = i
            i += 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 1 )
    return m
