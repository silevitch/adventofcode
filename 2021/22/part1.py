file = open("input.txt", "r")

# The data is decently sized so a dict is fine 
on = {}

for line in file:
    ####
    # data munging - I'm sure there is a better way to do this
    #

    type, data = line.strip().split(' ')
    
    dimensions = data.split(',')

    cuboid = []

    for dim in dimensions:
        pos, cordinates = dim.split('=')
        cuboid.append(cordinates.split('..'))
        cuboid[-1][0] = int(cuboid[-1][0])
        cuboid[-1][1] = int(cuboid[-1][1])
    
    #
    #    
    ####
    
    print(cuboid)

    # Brute force!
    for x in range(cuboid[0][0], cuboid[0][1] + 1):
        if x < -50 or x > 50:
            continue
        for y in range(cuboid[1][0], cuboid[1][1] + 1):
            if y < -50 or y > 50:
                continue
            for z in range(cuboid[2][0], cuboid[2][1] + 1):
                if z < -50 or z > 50:
                    continue
              
                key = str(x) + '_' + str(y) + '_' + str(z)
                
                if type == 'on':
                    on[ key ] = 1
                else:
                    on.pop( key, None )

print(len(on))
