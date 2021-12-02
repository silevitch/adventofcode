file = open("input.txt", "r")

prev = None
increase_count = 0

for line in file:
    curr = int(line)
    if prev is not None and prev < curr:
        increase_count += 1

    prev = curr

print(increase_count)

