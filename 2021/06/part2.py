file = open("input.txt", "r")

fishes = []

for line in file:
    fishes = line.strip().split(',')

days = [0] * 9

for i in range(len(fishes)):
    days[int(fishes[i])] += 1

for day in range(256):
    print(day)

    new_days = [0] * 9

    for i in range(len(days)):
        print(days[i])
        if i == 0:
            new_days[6] += days[i]
            new_days[8] += days[i]
        else:
            new_days[i-1] += days[i]
      
    days = new_days

num_fish = 0

for day in days:
    num_fish += day

print(num_fish)
