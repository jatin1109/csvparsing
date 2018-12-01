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
            create_histogram(list_by_col, 0)
        elif columnanalyser(list_by_col[0]) == "strings":
            create_bargraph(list_by_col, 0)
        else:
            print("shit")

    
decisionmaker(list_of_lists_as_columns, list_of_lists_as_rows)
