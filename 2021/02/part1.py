file = open("input.txt", "r")

depth = 0
horizontal = 0

for line in file:
    data = line.split()

    if data[0] == 'forward':
        horizontal += int(data[1])
    elif data[0] == 'up':
        depth -= int(data[1])
    else:
        depth += int(data[1])

print(depth)
print(horizontal)

