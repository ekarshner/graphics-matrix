from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


print '-------------------------- TESTING matrix.py --------------------------'
print 'MAKING A NEW MATRIX m1'
m1 = new_matrix()
print_matrix( m1 )

print 'TURNING m1 INTO AN IDENTITY MATRIX'
ident( m1 )
print_matrix( m1 )

print 'MAKING A NEW RANDOM MATRIX m2'
m2 = new_rand_matrix()
print_matrix( m2 )

print 'MAKING A NEW RANDOM MATRIX m3'
m3 = new_rand_matrix()
print_matrix( m3 )

print 'MULTIPLYING m1 * m2'
matrix_mult(m1, m2)
print_matrix( m2 )

print 'MULTIPLYING m2 * m3'
matrix_mult(m2, m3)
print_matrix( m3 )
