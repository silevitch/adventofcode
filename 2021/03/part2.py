file = open("input.txt", "r")

inputs = []

for line in file:
   inputs.append(line.strip()) 

def find_oxygen(inputs):
    position = 0
    while len(inputs) > 1:
        most = find_common(inputs, position, 'most')
        inputs = [ x for x in inputs if x[position] == most ]
        position += 1

    return(inputs[0])

def find_co2(inputs):
    position = 0
    while len(inputs) > 1:
        least = find_common(inputs, position, 'least')
        inputs = [ x for x in inputs if x[position] == least ]
        position += 1

    return(inputs[0])

   

def find_common(inputs, position, type):
    ones = 0

    for input in inputs:
        if input[position] == '1':
            ones += 1
  
    if type == 'most':
        if ones > len(inputs) / 2:
            return '1'
        elif ones == len(inputs) / 2:
            return '1'
        else:
            return '0'
    else:
        if ones > len(inputs) / 2:
            return '0'
        elif ones == len(inputs) / 2:
            return '0'
        else:
            return '1'
    

oxygen = find_oxygen(inputs)
co2 = find_co2(inputs)

print(int(oxygen, 2) * int(co2, 2))
