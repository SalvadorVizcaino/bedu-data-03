import csv


# CONSTANT
FILENAME = 'employees.csv'

with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)