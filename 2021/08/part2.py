file = open("input.txt", "r")

# Looking at '7' and the 3 numbers with 6 segments, we can deduce '6'
# Looking at '1' and the 3 numbers with 5 segments, we can deduce '3'
# Looking at '6' and the 2 numbers left with 5 segments, we can deduce '5'
# Only one left with 5 segments, so must be '2'
# Looking at '4' and the 2 numbers with 6 segments, we can deduce '9'
# That only leaves '0'

def order_digits(digit):
    return "".join(sorted(digit))

def contains(candidate, check_num):
    for char in check_num:
        if char not in candidate:
            return 0

    return 1

total = 0

for line in file:
    data = line.strip().split('|')

    inputs = data[0].strip().split(' ')
    
    digits = [""] * 10 
    fives = []
    sixes = []

    for a_input in inputs:
        a_input = order_digits(a_input)
        length = len(a_input)

        if length == 2:
            digits[1] = a_input
        elif length == 4:
            digits[4] = a_input
        elif length == 3:
            digits[7] = a_input
        elif length == 7:
            digits[8] = a_input
        elif length == 5:
            fives.append(a_input)
        else:
            sixes.append(a_input)

    for six in sixes:
        if (contains(six, digits[4])):
            digits[9] = six
        elif(contains(six, digits[7])):
            digits[0] = six
        else:
            digits[6] = six

    for five in fives:
        if (contains(five, digits[1])):
            digits[3] = five
        elif (contains(digits[6], five)):
            digits[5] = five
        else:
            digits[2] = five

   
    digit_lookup = {}
    
    for i in range(len(digits)):
        digit_lookup[digits[i]] = str(i)

    outputs = data[1].strip().split(' ')

    final_num = ''

    for output in outputs:
        output = order_digits(output)
        final_num += digit_lookup[output]

    total += int(final_num)

print(total)
