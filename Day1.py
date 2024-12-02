input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2024/Day1/input1.txt', 'r').read()
splinput = input.split()                            #Create an array for each number of orig input
leftarray = []                                      #Create initial array of left column
rightarray = []                                     #Create initial array of right column
similararray = []                                  #Create initial array of similar

for x in range(len(splinput)):                      #Way of seperating and grouping every other number (using even/odd "i")
    if(x%2) != 0:
        rightarray.append(int(splinput[x]))
    if (x % 2) == 0:
        leftarray.append(int(splinput[x]))

leftarray.sort()                                    #Unnecessary for Part2
rightarray.sort()

for i in leftarray:                                 #For each number in left column, count how many times it appears in right. Multiply and append similarity array
    count = 0                                       #Initiate counter
    for j in rightarray:
        if i == j:
            count+=1
    similarTotal = count*i
    similararray.append(similarTotal)
# print(leftarray)
# print(rightarray)
# print(similararray)
print('The total distance of the two locations is,', sum(similararray))
