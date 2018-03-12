import csv #imports module csv
from collections import OrderedDict

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t" #set your own delimiter

oldFile = csv.reader(open(filea,"r"),delimiter=delim)
next(oldFile)
newFile = csv.reader(open(fileb,"r"),delimiter=delim)
#open csv readers

oldFileAsList = []
newFileAsList = []

# prepare changes from file B
for row in oldFile:
    oldFileDict = OrderedDict()
    for i in range (0, 9):
        oldFileDict[i] = row[i]
    oldFileAsList.append(oldFileDict)
#print(oldFileAsList[1][1])

for row in newFile:
    newFileDict = OrderedDict()
    for i in range (0, 9):
        newFileDict[i] = row[i]
    newFileAsList.append(newFileDict)
#print(newFileAsList[0][1])

# write new changed rows
with open(output, "w") as fileoutput:
    csvwriter = csv.writer(fileoutput, delimiter=delim, quoting=csv.QUOTE_ALL)
    for personNewDict in newFileAsList:
        for index, personOldDict in enumerate(oldFileAsList):
            # needs to check whether there are any changes prepared
            if personNewDict[1][1] in personOldDict[2][1]:
                # change the item
                print(oldFileAsList[index][0])
                print(personNewDict)
                parsableFileAsList = personNewDict
                print(parsableFileAsList)
                keys, values = [], []
                for key, value in parsableFileAsList.items():
                    keys.append(key)
                    values.append(value)
                csvwriter.writerow(values)

""" print("\n")
outputfile = open(output)
outputreader = csv.reader(outputfile, delimiter=delim)
outputdata = list(outputreader)
for row in outputdata:
    print(str(row)) """