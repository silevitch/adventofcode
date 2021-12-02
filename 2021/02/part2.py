file = open("input.txt", "r")

depth = 0
horizontal = 0
aim = 0

for line in file:
    data = line.split()
    value = int(data[1])

    if data[0] == 'forward':
        horizontal += value
        depth += aim * value
    elif data[0] == 'up':
        aim -= value
    else:
        aim += value 

print(depth)
print(horizontal)

