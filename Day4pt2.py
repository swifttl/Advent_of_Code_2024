import math
input = open('input4', 'r').read()
grid =input.split('\n')
occurances = 0
for y in range(len(grid)):
    line = grid[y]
    for x in range(len(line)):
        ldiagArray = []
        rdiagArray = []
        bothArray = []
        if line[x] == 'A':
            if (x-1)<0 or (x+1)>len(line) or (y-1)<0:
                continue
            try:
                ldiagArray.extend([grid[y-1][x-1], grid[y][x], grid[y+1][x+1]])
                rdiagArray.extend([grid[y-1][x+1], grid[y][x], grid[y+1][x-1]])
                if ldiagArray == ['M', 'A', 'S'] or ldiagArray == ['S', 'A', 'M']:
                    bothArray.append(1)
                if rdiagArray == ['M', 'A', 'S'] or rdiagArray == ['S', 'A', 'M']:
                    bothArray.append(1)
                if sum(bothArray) == 2:
                    occurances +=1
            except IndexError:
                continue
print('The number of occurances is:', occurances)