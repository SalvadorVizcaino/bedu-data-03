import csv


# CONSTANT
FILENAME = 'writing_csv.csv'
COLUMN_NAMES = ['employee_id', 'entered_at', 'enter_for']
MAX_NUMBER_LOGS = 100

with open(FILENAME, mode='w',newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=COLUMN_NAMES)

    # WRITING HEADERS
    writer.writeheader()
    counter = 1
    while counter <= MAX_NUMBER_LOGS:
        writer.writerow({
            'employee_id': 1002, 
            'entered_at': 716253576253, 
            'enter_for': 'LUNCH'
        })
        counter += 1  # or counter = counter + 1