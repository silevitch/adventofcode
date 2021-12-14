import re

file = open("input.txt", "r")

dots = []
folds = []
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
        data = line.strip().split(' ')
        folds.append(data[2].split('='))

page = []

for line in range(max_y + 1):
    page.append(['.'] * ( max_x + 1 ))

for dot in dots:
    page[ dot[1] ][ dot[0] ] = '#'

def print_page(page):
    for line in page:
        print(''.join(line))

def do_fold(page, type, num):
    new_page = []
    print(type)
    print(num)
    print(len(page))
    print()

    if type == 'x':
        for line in range(len(page)):
            new_page.append( page[line][0:( num )] )
            fold_line = page[line][( num + 1 ):( max_x + 1) ]
      
            for i in range(len(fold_line)):
                if fold_line[i] == '#':
                    new_page[line][(len(new_page[-1]) - 1) - i] = '#'
    else:
        new_page = page[0:( num )]
        fold_line = page[( num + 1 ):( max_y + 1) ]

        for i in range(len(fold_line)):
            for j in range(len(fold_line[i])):
                if fold_line[i][j] == '#':
                    new_page[ len(new_page) - i - 1 ][j] = '#'

    print(len(new_page))
    return(new_page)

print_page(page)
for fold in folds:
    page = do_fold(page, fold[0], int(fold[1]))
    print_page(page)

