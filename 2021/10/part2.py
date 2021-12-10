file = open("input.txt", "r")


def is_open(char):
    if char == '(' or char == '[' or char == '{' or char == '<':
        return 1
    
    return 0

def is_matching_close(open_char, close_char):
    matches = { '()' : 1, '[]': 1, '{}' : 1, '<>' : 1 }
    
    if open_char + close_char in matches:
        return 1

    return 0

scores = []

points = { '(' : 1, '[' : 2, '{' : 3, '<' : 4 }

for line in file:
    syntax = line.strip()

    chunks = []

    incomplete = 1

    for char in syntax:
        if is_open(char):
            chunks.append(char)
        elif is_matching_close(chunks[-1], char):
            chunks.pop()
        else:
            incomplete = 0
            break

    if incomplete:
        print(chunks)

        chunk_score = 0

        for char in reversed(chunks):
            chunk_score *= 5
            chunk_score += points[ char ]

        scores.append(chunk_score)

scores.sort()
print(scores[ int(len(scores) / 2 ) ])
