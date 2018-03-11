import csv #imports module csv

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t" #set your own delimiter

source1 = csv.reader(open(filea,"r"),delimiter=delim)
next(source1)
source2 = csv.reader(open(fileb,"r"),delimiter=delim)
#open csv readers

source2_dict = {}

# prepare changes from file B
for row in source2:
    for x in range (1, 9):
        source2_dict[row[x]] = row[x]
    print(source2_dict)   
    
# write new changed rows
with open(output, "w") as fout:
    csvwriter = csv.writer(fout, delimiter=delim, quoting=csv.QUOTE_ALL)
    for row in source1:
        # needs to check whether there are any changes prepared
        for x in range(1,9):
            if row[x] in (None, ""):
                print("Row "+ row[0]+", column " + str(x) + " is empty.")
        if row[2] in source2_dict:
            # change the item
            for x in range(1,9):
                row[x] = "helo?"
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