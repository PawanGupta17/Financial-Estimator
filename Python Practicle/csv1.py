import csv as cv
csv_columns = ['No','Name','Country']
dict_data = [
{'No': 1, 'Name': 'Alex', 'Country': 'India'},
{'No': 2, 'Name': 'Ben', 'Country': 'USA'},
{'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
{'No': 4, 'Name': 'Smith', 'Country': 'USA'},
{'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
]
csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = cv.DictWriter(csvfile,csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
    print('rewev')
except IOError:
    print("I/O error")
