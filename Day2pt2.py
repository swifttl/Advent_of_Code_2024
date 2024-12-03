input = open('C:/Users/Terry/PycharmProjects/Projects/AdventofCode2024/Day2/input2', 'r').read()
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
#^Part One. V Part Two
#Kept P1 as it already provided structure to separate intial safe/unsafe
    else:
        for j in range(len(reports)):
            tempReports = []
            tempAscDesc = []
            tempDiff = []
#Create new lists, removing one item from reports at a time
            for k in range(len(reports)):
                tempReports.append(reports[k])
            tempReports.pop(j)
#Rerun the checker from Part One against each new list
            for x in range(0, len(tempReports) - 1, 1):
                if int(tempReports[x]) > int(tempReports[x + 1]):
                    tempAscDesc.append("yes")
                elif int(tempReports[x]) == int(tempReports[x + 1]):
                    tempAscDesc.append("same")
                else:
                    tempAscDesc.append("no")
            for x in range(0, len(tempReports) - 1, 1):
                if abs(int(tempReports[x]) - int(tempReports[x + 1])) < 4:
                    tempDiff.append("yes")
                else:
                    tempDiff.append("no")
            if len(set(tempAscDesc)) == 1 and set(tempAscDesc) != {'same'} and set(tempDiff) == {'yes'}:
                reportsarray.append("safe")
#Important to break, as some list have multiple possibilities to become safe; Would create duplicates
                break

print('The number of safe reports is', len(reportsarray))
