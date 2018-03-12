<<<<<<< HEAD
import csv
=======
import csv 
from pprint import pprint
>>>>>>> 28d9924401da82388725a365b1e3b4d947198838
from collections import OrderedDict

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t"

<<<<<<< HEAD
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
=======
source1 = csv.reader(open(filea,"r"),delimiter=delim)
next(source1)
source2 = csv.reader(open(fileb,"r"),delimiter=delim)

source_1_as_list = []
source_2_as_list = []

for row in source2:
    source2_dict = OrderedDict()
    for x in range (0, 9):
        source2_dict[x] = row[x]
    source_2_as_list.append(source2_dict)



for row in source1:
    source1_dict = OrderedDict()
    for x in range (0, 9):
        source1_dict[row[x]] = row[x]
    source_1_as_list.append(source1_dict)


for person_dict_new in source_2_as_list:
    for index, person_dict_old in enumerate(source_1_as_list):
        if(person_dict_new[2] in person_dict_old):
            #print(person_dict_new)
            source_1_as_list[index] = person_dict_new
            print(source_1_as_list)


# write new changed rows
with open(output, "w") as fout:
    csvwriter = csv.writer(fout, delimiter=delim, quoting=csv.QUOTE_ALL)
    for person_dict_new in source_2_as_list:
        for index, person_dict_old in enumerate(source_1_as_list):
            if(person_dict_new[2] in person_dict_old):
                #print(person_dict_new)
                source_1_as_list[index] = person_dict_new
                print(source_1_as_list)
                csvwriter.writerow(person_dict_new)

"""    
    for row in source1:
        print(row)
        # needs to check whether there are any changes prepared
        for x in range(0,9):
            if row[x] in (None, ""):
                print("Row "+ row[0]+", column " + str(x) + " is empty.")
        
        if row[2] in source2_dict:
            # change the item
            for x in range(0,9):
                row[x] = source2_dict[row[x]] 
>>>>>>> 28d9924401da82388725a365b1e3b4d947198838
        csvwriter.writerow(row)
"""

outputfile = open(output)
outputreader = csv.reader(outputfile, delimiter=delim)
outputdata = list(outputreader)
for row in outputdata:
<<<<<<< HEAD
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
=======
    print(str(row))
>>>>>>> 28d9924401da82388725a365b1e3b4d947198838
