file = open("input.txt", "r")

map = []

for line in file:
    data = line.strip()

    map.append([])

    for i in data:
        map[len(map) - 1].append(int(i))

risk = 0

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
    
        risk += cur_val + 1

print(risk)

