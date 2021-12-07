file = open("input.txt", "r")

crabs = []

for line in file:
    crabs = line.strip().split(',')

max_horizontal = 0

for i in range(len(crabs)):
    crabs[i] = int(crabs[i])

    if crabs[i] > max_horizontal:
        max_horizontal = crabs[i]

min_fuel = None
min_pos = None

for i in range(max_horizontal):
    fuel = 0
    for crab in crabs:
        for j in range(abs(crab - i)+1):
            fuel += j
            
            if min_fuel is not None and fuel > min_fuel:
                break
        if min_fuel is not None and fuel > min_fuel:
                break

    if min_fuel is None or fuel < min_fuel:
        min_fuel = fuel
        min_pos = i

print(min_fuel)
print(min_pos)
