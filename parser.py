import csv
import numpy as np
import matplotlib.pyplot as plt

def RepresentsInt(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False
file = csv.reader(open('student_data.csv'))
list_of_lists_as_rows = [] 
list_of_lists_as_columns = []
no_of_columns = 0
for row in file:
    row1 = row
    for i in row1:
        if RepresentsInt(i):
            i = float(i)
    list_of_lists_as_rows.append(row1)
    no_of_columns = len(row)
    
for i in range(no_of_columns):
    file1 = csv.reader(open('student_data.csv'))
    column = []
    x = 1
    for row in file1:
        if x == 1:
            x += 1
            continue
        if RepresentsInt(row[i]):
            row[i] = float(row[i])
        column.append(row[i])
    list_of_lists_as_columns.append(column)
    
print(list_of_lists_as_rows)
print(list_of_lists_as_columns)
