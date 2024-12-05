import re
input = open('input3', 'r').read()
mulRegex = r'(mul)[(](\d+)[,](\d+)[)]'
sumArray = []
# clean = "".join([x[x.find("do()") :] for x in (input).split("don't()")])
doArray = []

#new adds a starter "do()" and splits input at "don't()",
#making a list of elements before and after
new = ("do()"+input).split("don't()")

#for each item in the list (input split by don't())
for x in new:
    #x.find('do()') >>> returns the ~index of first occurance
    #x[x.find("do()"):] >>> for the string x at location of the first occurance
    #   of "do()" through the end of the string (which will have been shortened
    #   up to the occurance of "don't()")
    do = x[x.find("do()"):]
    #adding the peices to an Array so they can be catenated via "final"
    doArray.append(do)
    final = ''.join(doArray)

#repeat process from Part One
occurances = re.findall(mulRegex, final)
for x in occurances:
    product = int(x[1])*int(x[2])
    sumArray.append(product)
print('The sum of all findings is:', sum(sumArray))
