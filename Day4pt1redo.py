import math
input = open('input4', 'r').read()
grid =input.split('\n')
occurances = 0
for y in range(len(grid)):
    line = grid[y]
    for x in range(len(line)):
        horArray = []
        try:
            horArray.extend([line[x], line[x+1], line[x+2], line[x+3]])
            if horArray == ['X', 'M', 'A', 'S'] or horArray == ['S', 'A', 'M', 'X']:
                occurances +=1
        except IndexError:
            break
    for x in range(len(line)):
        verArray = []
        try:
            verArray.extend([grid[y][x], grid[y+1][x], grid[y+2][x], grid[y+3][x]])
            if verArray == ['X', 'M', 'A', 'S'] or verArray == ['S', 'A', 'M', 'X']:
                occurances += 1
        except IndexError:
            break
    for x in range(len(line)):
        ldiagArray = []
        if (x-1)<0 or (x-2)<0 or (x-3)<0:
            continue
        try:
            ldiagArray.extend([grid[y][x], grid[y+1][x-1], grid[y+2][x-2], grid[y+3][x-3]])
            if ldiagArray == ['X', 'M', 'A', 'S'] or ldiagArray == ['S', 'A', 'M', 'X']:
                occurances += 1
                print(y,x,ldiagArray)
        except IndexError:
            break
    for x in range(len(line)):
        rdiagArray = []
        if (x+1)>len(line) or (x+2)>len(line) or (x+3)>len(line):
            continue
        try:
            rdiagArray.extend([grid[y][x], grid[y+1][x+1], grid[y+2][x+2], grid[y+3][x+3]])
            print(rdiagArray)
            if rdiagArray == ['X', 'M', 'A', 'S'] or rdiagArray== ['S', 'A', 'M', 'X']:
                occurances += 1
        except IndexError:
            break
print('The number of occurances is:', occurances)
