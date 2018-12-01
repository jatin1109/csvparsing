# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 13:09:43 2018

@author: mikyp
"""

def columnanalyser(col):
    if type(all(col)) == int:
        return("Integers!")
    elif type(all(col)) == float:
        return("Floats!")
    elif type(all(col)) == str:
        return("Strings!")
    else:
        return("A combination of shit")
        
def coltypes(list_by_col):
    list_types = []
    for col in list_by_col:
        list_types.append(columnanalyser(col))
        print(list_types)

#def decisionmaker(list_by_col, list_by_row):

    
