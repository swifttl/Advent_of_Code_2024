import re
input = open('input3', 'r').read().split('\n')
print(input)
sumArray = []
mulRegex = r'(mul)[(](\d+)[,](\d+)[)]'
for line in input:
    occurances = re.findall(mulRegex, line)
    print(occurances)
    for x in occurances:
        product = int(x[1])*int(x[2])
        sumArray.append(product)
print('The sum of all findings is:', sum(sumArray))
