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

matrix_mult(m1, m2)
print_matrix( m2 )
