import csv
from collections import OrderedDict

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t" #set your own delimiter

oldFile = csv.reader(open(filea,"r"),delimiter=delim)
next(oldFile)
newFile = csv.reader(open(fileb,"r"),delimiter=delim)
#open csv readers

oldFileAsDict = dict()
newFileAsDict = dict()

# prepare changes from file B
for row in oldFile:
    for i in range (0, 9):
        newFileAsDict[i+1] = row[i]
print(newFileAsDict.items())
    
# write new changed rows
with open(output, "w+") as fileoutput:
    csvwriter = csv.writer(fileoutput, delimiter=delim, quoting=csv.QUOTE_ALL)
    for row in oldFile:
        # needs to check whether there are any changes prepared
        """         
        for x in range(0, 9):
        if row[x] in (None, ""):
            print("Row "+ row[0]+", column " + str(x) + " is empty.")
        """
        print(row[2])
        if row[2] in newFileAsDict:
            # change the item
            for i in range(0, 9):
                row[i] = "helo?"
        csvwriter.writerow(row)

outputfile = open(output)
outputreader = csv.reader(outputfile, delimiter=delim)
outputdata = list(outputreader)
for row in outputdata:
    print(str(row))

    


""" 
fileKilde = "a.csv"
filePersoner = "b.csv"
output = "c.csv"

delim = "\t"

source1 = csv.reader(open(fileKilde,"r"), delimiter=delim)
source2 = csv.reader(open(filePersoner,"r"), delimiter=delim)

source2Dict = {}

for row in source1:
    source2Dict[row[0]] = row[1]
    print(source2Dict)

with open(output, "w") as fout:
    csvwriter = csv.writer(fout, delimiter=delim)
    for row in source1:
        if row[1] in source2Dict:
            row[3] = source2Dict[row[1]]
        csvwriter.writerow(row) """


"""
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
            if(personNewDict[0] in personOldDict):
                oldFileAsList[index] = personNewDict
                print(oldFileAsList)
                csvwriter.writenow(personNewDict)
"""