import copy

file = open("input.txt", "r")

total_on = 0

inputs = []

for line in file:
    ####
    # data munging - I'm sure there is a better way to do this
    #

    type, data = line.strip().split(' ')

    # this was helpful when debugging
    if type == '#on' or type == '#off':
        continue

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

    inputs.append([ type, cuboid ])

# this function figures out how many new 'on's based on the target cuboid and the list of the previous cuboids
# 
def find_on(target_cuboid, cuboids):
    target_type, target = target_cuboid

    # there is no overlap
    if target[0][0] > target[0][1] or target[1][0] > target[1][1] or target[2][0] > target[2][1]:
        return(0)
    
    # edge case with no overlap
    if target[0][0] == target[0][1] and target[1][0] == target[1][1] and target[2][0] == target[2][1]:
        return(0)
   
    # if 'on', this is the max number of 'on's
    on = (target[0][1] - target[0][0] + 1) * (target[1][1] - target[1][0] + 1) * (target[2][1] - target[2][0] + 1)
    
    # if 'off', then there are no 'on's
    if target_type == 'off':
        on = 0

    if len(cuboids) == 0:
        return(on)

    # loop through the previous cuboids and see if they fit in the target
    for cuboid in cuboids:
        type, pos = cuboid

        if pos[0][0] < target[0][0]:
            pos[0][0] = target[0][0]

        if pos[0][1] > target[0][1]:
            pos[0][1] = target[0][1]
        
        if pos[1][0] < target[1][0]:
            pos[1][0] = target[1][0]

        if pos[1][1] > target[1][1]:
            pos[1][1] = target[1][1]

        if pos[2][0] < target[2][0]:
            pos[2][0] = target[2][0]

        if pos[2][1] > target[2][1]:
            pos[2][1] = target[2][1]
  
    # now with the adjusted positions, let's subtract the overlaping 'on's
    for i in range(len(cuboids)):
        on -= find_on(cuboids[i], copy.deepcopy(cuboids[0:i]))

    return(on)

grand_total = 0

# We will find the 'on's for the first item, then add the 'on's that are unique to the second item taking into account the first item, etc
# For 'off's, find_on will return negative
for i in range(len(inputs)):
    total = find_on(inputs[i], copy.deepcopy(inputs[0:i]))
    print(total)
    grand_total += total

print()
print(grand_total)

