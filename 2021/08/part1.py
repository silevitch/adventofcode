file = open("input.txt", "r")

digits = 0

for line in file:
    data = line.strip().split('|')

    outputs = data[1].strip().split(' ')

    for output in outputs:
        length = len(output)

        if length == 2 or length == 4 or length == 3 or length == 7:
            digits += 1

print(digits)

