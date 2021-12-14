import re

file = open("input.txt", "r")

dots = []
max_x = 0
max_y = 0

for line in file:
    if re.search(',', line):
        dot = line.strip().split(',')

        dot[0] = int(dot[0])
        dot[1] = int(dot[1])

        dots.append(dot)

        if dot[0] > max_x:
            max_x = dot[0]
        if dot[1] > max_y:
            max_y = dot[1]
    elif re.search('fold', line):
        print(line)

page = []

for line in range(max_y + 1):
    page.append(['.'] * ( max_x + 1 ))

for dot in dots:
    page[ dot[1] ][ dot[0] ] = '#'

def count_dots(page):
    count = 0
    for line in page:
        for space in line:
            if space == '#':
                count += 1
    return count

def do_fold(page, type, num):
    new_page = []
    if type == 'x':
        for line in range(len(page)):
            new_page.append( page[line][0:( num - 1 )] )
            fold_line = page[line][( num + 1 ):( max_x + 1) ]

            for i in range(len(fold_line)):
                if fold_line[i] == '#':
                    new_page[line][(num - 1) - i] = '#'

        return(new_page)

page = do_fold(page, 'x', 655)

print(count_dots(page))
