import csv 
from pprint import pprint
from collections import OrderedDict

filea = "1.csv"
fileb = "2.csv"
output = "3.csv"

delim = "\t"

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
        csvwriter.writerow(row)
"""

outputfile = open(output)
outputreader = csv.reader(outputfile, delimiter=delim)
outputdata = list(outputreader)
for row in outputdata:
    print(str(row))