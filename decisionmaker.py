# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:09:43 2018

@author: mikyp
"""

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
    file1 = csv.reader(open("student_data.csv"))
    column = []
    x = 1
    for row in file1:
        if x == 1:
            x += 1
            continue
        column.append(row[i])
    list_of_lists_as_columns.append(column)
    
def columnanalyser(col):
    
    if all(type(i) is int for i in col):
        return("ints")
    elif all(type(i) is float for i in col):
        return("floats")
    elif all(type(i) is str for i in col):
        return("strings")
    else:
        return("shit")

def coltypes(list_by_col):
    list_types = []
    for col in list_by_col:
        list_types.append(columnanalyser(col))
    print(list_types)

def decisionmaker(list_by_col, list_by_row):
    cols_num = len(list_by_col)
    if cols_num == 1:
        if columnanalyser(list_by_col[0]) == "ints" or "floats":
            #create_histogram(list_by_col, 0)
        elif columnanalyser(list_by_col[0]) == "strings":
            #create_bargraph(list_by_col, 0)
        else:
            print("shit")
