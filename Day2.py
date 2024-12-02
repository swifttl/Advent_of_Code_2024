input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2024/Day1/input1.txt', 'r').read()
splinput = input.split()                            #Create an array of each number
leftarray = []                                      #Create initial array of left column
rightarray = []                                     #Create initial array of right column
distancearray = []                                  #Create initial array of difference(distance)

for x in range(len(splinput)):                      #Way of seperating and grouping every other number (using even/odd "i")
    if(x%2) != 0:
        rightarray.append(int(splinput[x]))
    if (x % 2) == 0:
        leftarray.append(int(splinput[x]))

leftarray.sort()                                    #Sorting in order of lowest to highest
rightarray.sort()

for i in range(len(leftarray)):                     #Math portion and appending distancearray
    distancearray.append(abs(leftarray[i] - rightarray[i]))
# print(leftarray)
# print(rightarray)
# print(distancearray)

print('The total distance of the two locations is,', sum(distancearray))
