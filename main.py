from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print('print_matrix')
m1 = new_matrix()
print_matrix( m1 )

print('ident')
ident( m1 )
print_matrix( m1 )

m1 = new_matrix()
random_matrix(m1)
m2 = new_matrix(4,2)
random_matrix(m2)

print('this is m1')
print_matrix(m1)
print('this is m2')
print_matrix(m2)

print('matrix_mult m1 * m2')
matrix_mult(m1, m2)
print_matrix( m2 )

m3 = new_matrix()
random_matrix(m3)
print('m3')
print_matrix(m3)
print('add_point')
add_point(m3,0,0,0)
print_matrix(m3)

print('add_edge')
add_edge(m3,1,1,1,2,2,2)
print_matrix(m3)


#make starburst
