file = open("input.txt", "r")

ones = []
count = 0

for line in file:
    count += 1
    
    # -1 in range is so that we don't iterate over the \n character
    for char in range(len(line) - 1):

        if char == len(ones):
            ones.append(0)

        if line[char] == '1':
            ones[char] += 1

gamma = ''
epsilon = ''

for i in ones:
    if i > count / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(int(gamma,2) * int(epsilon,2))
