file = open("input.txt", "r")

prev = 9999999999999 
increase_count = 0

for line in file:
    curr = int(line)
    if prev < curr:
        increase_count += 1

    prev = curr

print(increase_count)

