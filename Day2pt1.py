input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2024/Day2/prompt1', 'r').read()
reportsarray = []

for r in input.splitlines():
    reports = r.split()
    rAscDescarray = []
    rDiffArray = []
    for i in range(0,len(reports)-1, 1):
        if int(reports[i])>int(reports[i+1]):
            rAscDescarray.append("yes")
        elif int(reports[i])==int(reports[i+1]):
            rAscDescarray.append("same")
        else:
            rAscDescarray.append("no")
    for i in range(0, len(reports) - 1, 1):
        if abs(int(reports[i])-int(reports[i+1])) < 4:
            rDiffArray.append("yes")
        else:
            rDiffArray.append("no")

    if len(set(rAscDescarray)) == 1 and set(rDiffArray) == {'yes'}:
        reportsarray.append("safe")


print('The number of safe reports is', len(reportsarray))
