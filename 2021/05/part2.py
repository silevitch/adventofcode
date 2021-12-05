file = open("input.txt", "r")

ocean = {}
twos = 0

def inc_ocean(key):
    if key not in ocean:
        ocean[ key ] = 0

    ocean[ key ] += 1

    print(key + " " + str(ocean[ key ]))
    if ocean[ key ] == 2:
        return 1

    return 0

for line in file:
    vent = line.strip().split()
    first_pt = vent[0].split(',')
    second_pt = vent[2].split(',')
    
    xs = [ int(first_pt[0]), int(second_pt[0]) ]
    ys = [ int(first_pt[1]), int(second_pt[1]) ]

    if xs[0] == xs[1]:
        print("0 is the same")
 
        min_y = ys[0]
        max_y = ys[1]
        if ys[0] > ys[1]:
            min_y = ys[1]
            max_y = ys[0]
       
        for i in range(min_y, max_y + 1):
            twos += inc_ocean( str(xs[0]) + "_" + str(i) )
    elif ys[0] == ys[1]:
        print("1 is the same")
        
        min_x = xs[0]
        max_x = xs[1]
        if xs[0] > xs[1]:
            min_x = xs[1]
            max_x = xs[0]
        
        for i in range(min_x, max_x + 1):
            twos += inc_ocean( str(i) + "_" + str(ys[0]) )
    else:
        x_mv = 1
        y_mv = 1

        if xs[0] > xs[1]:
            x_mv = -1
        if ys[0] > ys[1]:
            y_mv = -1

        x_cur = xs[0]
        y_cur = ys[0]

        while x_cur != xs[1] + x_mv:
            twos += inc_ocean( str(x_cur) + "_" + str(y_cur) )

            x_cur += x_mv
            y_cur += y_mv
        
print(twos)

