file = open("input.txt", "r")

caves = {}

for line in file:
    data = line.strip().split('-')

    if data[0] != 'end':
        if data[0] in caves:
            caves[ data[0] ].append( data[1] )
        else:
            caves[ data[0] ] = [ data[1] ]
   
    if data[0] != 'start':
        if data[1] in caves:
            caves[ data[1] ].append( data[0] )
        else:
            caves[ data[1] ] = [ data[0] ]

completed = []

def do_path(path, new):
    new_path = path.copy()
    if new == 'end':
        new_path.append(new)
        completed.append(new_path)
        return

    if new == new.lower():
        small_caves = {}
        double = 0

        for cave in new_path:
            if cave == cave.lower():
                if cave in small_caves:
                    double = 1
                else:
                    small_caves[ cave ] = 1
   
        if double:
           for cave in new_path:
                if cave == new:
                    return
    
    new_path.append( new )
    
    for cave in caves[ new ]:
        do_path(new_path, cave)

do_path([], 'start')

print(len(completed))
