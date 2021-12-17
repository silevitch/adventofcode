min_target_x = 70
max_target_x = 125
min_target_y = -159
max_target_y = -121

#min_target_x = 20
#max_target_x = 30
#min_target_y = -10
#max_target_y = -5


max_y = None 
hits = 0

def move(x, y, v_x, v_y, this_max_y):
    global max_y
    global hits

    x += v_x
    y += v_y
 
    if y > this_max_y:
        this_max_y = y
   
    # if x velocity is 0 and x isn't within the target then it can never hit
    if v_x == 0 and ( x > max_target_x or x < min_target_x ):
        return(0)

    # yay, we are in the target range
    if y >= min_target_y and y <= max_target_y and x >= min_target_x and x <= max_target_x:
        print('Hit Target!')
        hits += 1

        if max_y == None or this_max_y > max_y:
            max_y = this_max_y
        
        return(1)

    if ( y < min_target_y ) and v_x == 0 :
        print('Miss')
        return(0)

    if x > max_target_x and v_x > 0 : 
        print('Miss')
        return(0)

    if v_x > 0:
        v_x -= 1
    elif v_x < 0:
        v_x += 1

    v_y -= 1

    return( move(x, y, v_x, v_y, this_max_y) )

for x in range(max_target_x):
    for y in range(abs(min_target_y) + 1):
        
        hit_flag = move(0, 0, x + 1 , y, 0)
        if hit_flag:
            print('start x=' + str(x + 1) + ' start y=' + str(y))
       
        if y != 0:
            hit_flagi = move(0, 0, x + 1, -1 * y, 0)
            if hit_flag:
                print('start x=' + str(x + 1) + ' start y=' + str(-1*y))

print(max_y)
print(hits)
