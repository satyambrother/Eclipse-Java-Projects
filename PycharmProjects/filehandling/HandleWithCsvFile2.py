import csv
f=open('csvfile.csv','r')
r=csv.reader(f)
data=list(r)
for row in data:
    for column in row:
        print(column,'\t',end='')
    print()

        #print(row[0],row[1],row[2],row[3],sep='\t')