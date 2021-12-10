file = open("input.txt", "r")


def is_open(char):
    if char == '(' or char == '{' or char == '<' or char == '[':
        return 1
    
    return 0

def is_matching_close(open_char, close_char):
    matches = { '[]' : 1, '<>' : 1, '{}' : 1, '()' : 1 }
    
    if open_char + close_char in matches:
        return 1

    return 0

score = 0

points = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }

for line in file:
    syntax = line.strip()

    chunks = []

    for char in syntax:
        if is_open(char):
            chunks.append(char)
        elif is_matching_close(chunks[-1], char):
            chunks.pop()
        else:
            print('Corrupt!')
            score += points[ char ]
            break

print(score)
