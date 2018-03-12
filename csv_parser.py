import csv
from collections import OrderedDict

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t"

oldFile = csv.reader(open(filea,"r"),delimiter=delim)
next(oldFile)
newFile = csv.reader(open(fileb,"r"),delimiter=delim)

oldFileAsList = []
newFileAsList = []

for row in newFile:
    newFileDict = OrderedDict()
    for i in range (0, 9):
        newFileDict[i] = row[i]
    newFileAsList.append(newFileDict)

for row in oldFile:
    oldFileDict = OrderedDict()
    for i in range (0, 9):
        oldFileDict[row[i]] = row[i]
    oldFileAsList.append(oldFileDict)

for personNewDict in newFileAsList:
    for index, personOldDict in enumerate(oldFileAsList):
        if(personNewDict[2]) in personOldDict:
            oldFileAsList[index] = personNewDict

with open(output, "w") as fileoutput:
    csvwriter = csv.writer(fileoutput, delimiter=delim, quoting=csv.QUOTE_ALL)
    for personNewDict in newFileAsList:
        for index, personOldDict in enumerate(oldFileAsList):
            if(personNewDict[2] in personOldDict):
                oldFileAsList[index] = personNewDict
                print(oldFileAsList)
            csvwriter.writenow(personNewDict)