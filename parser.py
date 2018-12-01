import csv
import numpy as np
import matplotlib.pyplot as plt

file = csv.reader(open('student_data.csv'))
list_of_lists_as_rows = [] 
list_of_lists_as_columns = []
no_of_columns = 0
for row in file:
    list_of_lists_as_rows.append(row)
    no_of_columns = len(row)
    
for i in range(no_of_columns):
    file1 = csv.reader(open('student_data.csv'))
    column = []
    x = 1
    for row in file1:
        if x == 1:
            x += 1
            continue
        column.append(row[i])
    list_of_lists_as_columns.append(column)
    
print(list_of_lists_as_rows)
print(list_of_lists_as_columns)
