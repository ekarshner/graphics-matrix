from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for i in range(0, len(matrix), 2):
        draw_line(matrix[i][0], matrix[i][1], matrix[i+1][0], matrix[i+1][1], screen, color)
    

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    point = [x, y, z, 1]
    matrix.append(point)



def draw_line( x0, y0, x1, y1, screen, color ):
    if(x0 > x1):
        temp = x0
        x0 = x1
        x1 = temp
        temp = y0
        y0 = y1
        y1 = temp

    a = y1 - y0
    b = x1 - x0
    #vertical line
    if (b == 0):
        if(y0 < y1):
            while(y0 < y1):
                plot(screen, color, x0, y0)
                y0 += 1
        else:
            while(y1 < y0):
                plot(screen, color, x0, y1)
                y1 += 1
        return
    m = a / b
    #print("a = ", a, "b = ", b, "m = ", m)


    #octant1
    if (m >= 0 and m <=1):
        d = 2 * a - b
        #print d, x0, x1
        while (x0 <= x1):
            plot(screen, color, x0, y0)
            if(d > 0):
                y0 += 1
                d -= 2 * b
            x0 += 1
            d += 2 * a
        return

    #octant2
    if (m > 1):
        d = 2 * b + a
        #print d, y0, y1
        while (y0 >= y1):
            plot(screen, color, x0, y0)
            if(d < 0):
                x0 += 1
                d += 2 * a
            y0 += 1
            d -= 2 * b
        return

    #octant7
    if (m < -1):
        d = a + 2 * b
        #print d, x0, x1
        while (y0 >= y1):
            plot(screen, color, x0, y0)
            if(d > 0):
                x0 += 1
                d += 2 * a
            y0 -= 1
            d += 2 * b
        return

    #octant8
    if (m >= -1 and m < 0):
        d = 2 * a - b
        #print d, x0, x1
        while (x0 <= x1):
            plot(screen, color, x0, y0)
            if(d < 0):
                y0 -= 1
                d += 2 * b
            x0 += 1
            d += 2 * a
        return
