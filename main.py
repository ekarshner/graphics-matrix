from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


m1 = new_matrix()
print_matrix( m1 )

ident( m1 )
print_matrix( m1 )

m1 = new_matrix()

m2 = new_matrix(4,2)
matrix_ordered(m2)

print_matrix(m1)
print('this is m2')
print_matrix(m2)

matrix_mult(m1, m2)
print_matrix( m2 )
