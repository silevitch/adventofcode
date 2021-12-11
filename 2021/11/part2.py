file = open("input.txt", "r")

map = []

for line in file:
    line = line.strip()

    map.append([])

    for i in line:
        map[-1].append(int(i))

def do_flash(row, col):
    global flashes
    flashes += 1

    if row - 1 >= 0 and col - 1 >= 0:
        increment(row - 1, col - 1)
    if row - 1 >= 0 and col + 1 < len(map[0]):
        increment(row - 1, col + 1)
    if col - 1 >= 0:
        increment(row, col - 1)
    if col + 1 < len(map[0]):
        increment(row, col + 1)
    if row - 1 >= 0:
        increment(row - 1, col)
    if row + 1 < len(map):
        increment(row + 1, col)
    if row + 1 < len(map) and col - 1 >= 0:
        increment(row + 1, col - 1)
    if row + 1 < len(map) and col + 1 < len(map[0]):
        increment(row + 1, col + 1)
        
def increment(row, col):
    map[row][col] += 1
    if map[row][col] == 10:
        do_flash(row, col)

def print_map():
    for row in range(len(map)):
        print(map[row])

    print()

flashes = 0
steps = 0

while flashes != 100:
    steps += 1
    flashes = 0

    for row in range(len(map)):
        for col in range(len(map[row])):
            increment(row, col)

    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] > 9:
                map[row][col] = 0

    print_map()

print(steps)
