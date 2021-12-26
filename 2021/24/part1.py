# 
# This puzzle is sneaky. I skipped making a program that implements the ALU rules because they are so simple.
# Instead I spent time (a lot of it) trying to figure out how to not brute force it. I realized that we need
# to make sure that everytime we see "eql x w" "eql x 0" we need to make sure that x is "0". This will stop 
# z from growing too large.
#

def find_first_x_zero(inputs):

    x = 0
    y = 0
    z = 0
    #inp w
    w = inputs[0]
    #add x z
    #mod x 26
    #div z 1
    #add x 10
    #eql x w
    #eql x 0
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    #mul y 0
    #add y w
    #add y 15
    #mul y x
    #add z y
    z += w + 15
    #inp w
    w = inputs[1]
    #mul x 0
    #add x z
    #mod x 26
    #div z 1
    #add x 12
    #eql x w
    #eql x 0
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= 26
    #mul y 0
    #add y w
    #add y 8
    #mul y x
    #add z y
    z += w + 8
    #inp w
    w = inputs[2]
    #mul x 0
    #add x z
    #mod x 26
    #div z 1
    #add x 15
    #eql x w
    #eql x 0
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= 26
    #mul y 0
    #add y w
    y = w
    #add y 2
    y += 2
    #mul y x
    #add z y
    z += y
    #inp w
    w = inputs[3]
    #mul x 0
    #add x z
    x = z
    #mod x 26
    x = x % 26
    #div z 26
    z = int(z / 26)
    #add x -9
    x -= 9
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    y = 25
    #mul y x
    y *= x
    #add y 1
    y += 1
    #mul z y
    z *= y
    #mul y 0
    #add y w
    #add y 6
    y = w + 6
    #mul y x
    y *= x
    #add z y
    z += y

    return( z, x )

def find_second_x_zero(z, inputs):
    #inp w
    w = inputs[0]
    #mul x 0
    #add x z
    #mod x 26
    x = 1 
    #div z 1
    #add x 15
    #eql x w
    #eql x 0
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    y = 26 
    #mul z y
    z *= y
    #mul y 0
    #add y w
    y = w
    #add y 13
    y += 13
    #mul y x
    #add z y
    z += y
    #inp w
    w = inputs[1]
    #mul x 0
    #add x z
    #mod x 26
    #div z 1
    #add x 10
    #eql x w
    #eql x 0
    x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= 26
    #mul y 0
    #add y w
    #add y 4
    #mul y x
    y = w + 4
    #add z y
    z += y
    #inp w
    w = inputs[2]
    #mul x 0
    #add x z
    #mod x 26
    #div z 1
    #add x 14
    #eql x w
    #eql x 0
    # x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= 26
    #mul y 0
    #add y w
    #add y 1
    #mul y x
    #add z y
    z += w + 1
    #inp w
    w = inputs[3]
    #mul x 0
    #add x z
    #mod x 26
    #div z 26
    #add x -5
    x = (z % 26) - 5
    z = int ( z / 26)
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    y = 25 * x + 1
    #mul z y
    z *= y
    #mul y 0
    #add y w
    #add y 9
    #mul y x
    y = x * (w + 9)
    #add z y
    z += y
    
    return(z, x)

def find_third_x_zero(z, inputs):
    #inp w
    w = inputs[0]
    #mul x 0
    #add x z
    #mod x 26
    #div z 1
    #add x 14
    #eql x w
    #eql x 0
    # x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= 26
    #mul y 0
    #add y w
    #add y 5
    #mul y x
    #add z y
    z += w + 5
    #inp w
    w = inputs[1]
    #mul x 0
    #add x z
    #mod x 26
    #div z 26
    x = ( z % 26 ) - 7
    z = int (z / 26)
    #add x -7
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    #mul z y
    z *= ((25 * x) + 1)
    #mul y 0
    #add y w
    #add y 13
    #mul y x
    y = ( w + 13 ) * x
    #add z y
    z += y

    return (z, x)

def find_fourth_x_zero(z, inputs):
    #inp w
    w = inputs[0]
    #mul x 0
    #add x z
    #mod x 26
    x = ( z % 26 ) - 12
    #div z 26
    z = int ( z / 26 )
    #add x -12
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    y = (25 * x ) + 1
    #mul z y
    z *= y
    #mul y 0
    #add y w
    #add y 9
    #mul y x
    y = x * ( w + 9 )
    #add z y
    z += y

    #inp w
    w = inputs[1]
    #mul x 0
    #add x z
    #mod x 26
    x = ( z % 26 ) - 10
    #div z 26
    z = int ( z / 26 )
    #add x -10
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    y = ( x * 25 ) + 1
    #mul z y
    z *= y
    #mul y 0
    #add y w
    #add y 6
    #mul y x
    y = x * ( w + 6 )
    #add z y
    z += y
    return( z, x)

def find_fifth_x_zero(z, inputs):
    #inp w

    w = inputs[0]
    #mul x 0
    #add x z
    #mod x 26
    x = ( z % 26 ) - 1
    #div z 26
    z = int ( z / 26 )
    #add x -1
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    y = ( 25 * x ) + 1
    #mul z y
    z *= y
    #mul y 0
    #add y w
    #add y 2
    #mul y x
    y = x * ( w + 2 )
    #add z y
    z += y
    #inp w
    w = inputs[1]
    #mul x 0
    #add x z
    #mod x 26
    x = ( z % 26 ) - 11
    #div z 26
    z = int ( z / 26 )
    #add x -11
    #eql x w
    #eql x 0
    if x == w:
        x = 0
    else:
        x = 1
    #mul y 0
    #add y 25
    #mul y x
    #add y 1
    y = ( 25 * x ) + 1
    #mul z y
    z *= y
    #mul y 0
    #add y w
    #add y 2
    #mul y x
    y = x * ( w + 2 )
    #add z y
    z += y

    return(z, x)


for a in range(9, 0, -1):
    for b in range(9, 0, -1):
        for c in range(9, 0, -1):
            for d in range(9, 0, -1):
                first_z, x = find_first_x_zero([ a, b, c, d ])
                if x == 0:
                    for e in range(9, 0, -1):
                        for f in range(9, 0, -1):
                            for g in range(9, 0, -1):
                                for h in range(9, 0, -1):
                                    second_z, x = find_second_x_zero(first_z, [ e, f, g, h ])
                                    if x == 0:
                                        for i in range(9, 0, -1):
                                            for j in range(9, 0, -1):
                                                third_z, x = find_third_x_zero(second_z, [ i, j ])
                                                if x == 0:
                                                    for k in range(9, 0, -1):
                                                        for l in range(9, 0, -1):
                                                            fourth_z, x = find_fourth_x_zero(third_z, [ k, l ])
                                                            if x == 0:
                                                                for m in range(9, 0, -1):
                                                                    for n in range(9, 0, -1):
                                                                        fifth_z, x = find_fifth_x_zero(fourth_z, [  m, n ])
                                                                        if fifth_z == 0:
                                                                            print([a,b,c,d,e,f,g,h,i,j,k,l,m,n])
                                                                            exit()
