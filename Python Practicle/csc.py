import csv
with open('Book1.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for line in csv_reader :
         csv_writer.writerow(line)
