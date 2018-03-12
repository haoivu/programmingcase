import csv #imports module csv
from pprint import pprint
from collections import OrderedDict

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t" #set your own delimiter

newFile = csv.reader(open(filea,"r"),delimiter=delim)
next(newFile)
oldFile = csv.reader(open(fileb,"r"),delimiter=delim)
#open csv readers

oldFileAsList = OrderedDict()
newFileAsList = OrderedDict()

# prepare changes from file B
for row in oldFile:
    for i in range (0 , 9):
        oldFileAsList[i+1] = row[i]

# write new changed rows
with open(output, "w") as fileoutput:
    csvwriter = csv.writer(fileoutput, delimiter=delim, quoting=csv.QUOTE_ALL)
    for row in newFile:
        # needs to check whether there are any changes prepared
        if row[1] in oldFileAsList:
            # change the item
            row[3] = oldFileAsList[row[1]]
        csvwriter.writerow(row)