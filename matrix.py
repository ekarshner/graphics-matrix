import math


def print_matrix( matrix ):
    final = ''
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            final += str(matrix[i][j]) + ' '
        final += '\n'
    print final

def ident( matrix ):
    new_matrix()
    for i in range(0, 4, 1):
        matrix[i][i] = 1

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    final = new_matrix(len(m1[0]), 1)




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
