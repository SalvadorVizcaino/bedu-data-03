# Given 10000 logs
# Group logs by employee
# Numer of each category 'enter_for' a employee has entered
# i.e. employee 1002 meeting - 52, call - 80
# Show hot hours for enter to the facilities

import csv
import pandas as pd
import numpy as np

# CONSTANTS
FILENAME = 'tmp/10000logs_csv.csv'

employeesdf = pd.read_csv(FILENAME)
# Group logs by employee
# Numer of each category 'enter_for' a employee has entered
# print(employeesdf.groupby('employee_id')['enter_for'].value_counts().unstack())

# Show hot hours for enter to the facilities
employeesdf['date'] = pd.to_datetime(employeesdf['entered_at'])

employeesdf['year'] = employeesdf['date'].dt.year
employeesdf['month'] = employeesdf['date'].dt.month
employeesdf['day'] = employeesdf['date'].dt.day
employeesdf['hour'] = employeesdf['date'].dt.hour

# print(employeesdf.groupby('enter_for')['hour'].value_counts().reset_index(name='Entradas'))

# hothour = employeesdf.groupby(['hour']).size().reset_index(name='Entradas')
# hothourby = employeesdf.groupby(['enter_for','hour']).size().reset_index(name='Entradas')

# print(hothour.describe().loc['max'])
# print(hothourby.describe())

# df_hothours = employeesdf.groupby(['enter_for'])['hour'].value_counts().reset_index(name='Entradas')

hothour = employeesdf.groupby(['hour'])['enter_for'].value_counts().reset_index(name='Entradas')
hothour1 = hothour.sort_values(['Entradas'],ascending=[False])
hothour2 = hothour1.groupby(['hour'])['Entradas'].sum().reset_index(name='Entradas')
hothour3 = hothour2.sort_values(['Entradas'],ascending=[False])
# print(f'The top 1 hot hours and qty for enter to the facilites are:')
# print(hothour3.head(3))

print(f'The top 3 hot hours for enter to the facilites are:')
n = 0
for top in hothour3[1:3]:
    n += 1
    print(f'{n}.-{top} hrs')

