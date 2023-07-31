import csv
test_file = 'Names.csv'
with open ('tempname.txt') as f:
    name=f.read()
with open(test_file, 'r')as c:
    csv_file = csv.DictReader(c)    
    for line in csv_file:
        if name==line['uname']:
            uname=line['uname']
            passw=line['password']
            mbno=line['mobno']
            

