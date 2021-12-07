file = open("input.txt", "r")

fishes = []

for line in file:
    fishes = line.strip().split(',')

for i in range(len(fishes)):
    fishes[i] = int(fishes[i])

print(fishes)
for day in range(80):
    print(day)
    # We need to find the total now because we will be adding new fish to the list
    total = len(fishes)
    for i in range(total):
        if fishes[i] == 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] -= 1
       
print(len(fishes))
