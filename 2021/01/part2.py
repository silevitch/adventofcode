file = open("input.txt", "r")

inputs = []

for line in file:
    inputs.append(int(line))

increase_count = 0

for i in range(len(inputs) - 3):
    if inputs[i] + inputs[i + 1] + inputs[i + 2] < inputs[i + 1] + inputs[i + 2] + inputs[i + 3]:
            increase_count += 1

print(increase_count)

