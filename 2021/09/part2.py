file = open("input.txt", "r")

map = []

for line in file:
    data = line.strip()

    map.append([])

    for i in data:
        map[len(map) - 1].append(int(i))

low_points = []

for row in range(len(map)):
    for i in range(len(map[row])):
        cur_val = map[row][i]

        if row != 0 and map[row - 1][i] <= cur_val:
            continue

        if row != len(map) - 1 and map[row + 1][i] <= cur_val:
            continue

        if i != 0 and map[row][i - 1] <= cur_val:
            continue

        if i != len(map[row]) - 1 and map[row][i + 1] <= cur_val:
            continue
   
        low_points.append([row, i])

def check_point(point):
    key = str(point[0]) + '_' + str(point[1])

    if map[point[0]][point[1]] != 9 and key not in basin:
            basin[ key ] = point

sizes = []

for low_point in low_points:
    basin = {}

    basin[ str(low_point[0]) + '_' + str(low_point[1]) ] = low_point

    count = 0

    while count != len(basin):
        count = len(basin)

        checks = []

        for key in basin:
            checks.append(basin[key])

        for point in checks:
            if point[0] != 0:
                check_point([ point[0] - 1, point[1] ])
            if point[0] != len(map) - 1:
                check_point([ point[0] + 1, point[1] ])
            if point[1] != 0:
                check_point([ point[0], point[1] - 1 ])
            if point[1] != len(map[0]) - 1:
                check_point([ point[0], point[1] + 1 ])

    sizes.append(count)

sizes.sort( reverse = True)

print(sizes[0] * sizes[1] * sizes[2])

