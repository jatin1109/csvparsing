import csv
import numpy as np
import matplotlib.pyplot as plt
import http.server
import socketserver
import re
import urllib.parse
import shutil
import os
from numpy.polynomial.polynomial import polyfit

path = ""
PORT = 8080
no_of_graphs = 1

def cleartmp():
    dirPath = os.path.realpath(__file__).replace("parser.py", "tmp")
    fileList = os.listdir(dirPath)
    for fileName in fileList:
        if (fileName != "file"):
            os.remove(dirPath + "/" + fileName)
cleartmp()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if(re.match(r'/graph.html.*',self.path) != None):
            path = re.findall(r'(?<=/graph.html\?path=).*', self.path)[0]
            path = urllib.parse.unquote(path).replace("+"," ")
            print(path)
            try:
                file = csv.reader(open(path))
            except:
                None

            def RepresentsInt(s):
                try:
                    float(s)
                    return True
                except ValueError:
                    return False

            file = csv.reader(open(path))
            list_of_lists_as_rows = []
            list_of_lists_as_columns = []
            
            no_of_columns = 0
            for row in file:
                row1 = row
                for i in range(len(row1)):
                    if RepresentsInt(row1[i]):
                        row1[i] = float(row1[i])
                list_of_lists_as_rows.append(row1)
                no_of_columns = len(row)

            for i in range(no_of_columns):
                file1 = csv.reader(open(path))
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

            # graphmaker
            def create_histogram(col):
                x_label = col[0]
                x_values = col[1:]
                global no_of_graphs
                no_of_graphs += 1
                plt.hist(x_values)
                plt.xlabel(x_label)
                plt.savefig('tmp\image' + str(no_of_graphs) + '.png')

            def create_bargraph(col):
                x_label = col[0]
                x_values1 = col[1:]
                global no_of_graphs
                no_of_graphs += 1
                frequency = []
                x_values = []
                for n in x_values1:
                    if n not in x_values:
                        frequency.append(x_values1.count(n))
                        x_values.append(n)
                x_count = len(x_values)
                plt.bar(range(x_count), frequency, width = 0.5)
                plt.xlabel(x_values)
                plt.ylabel(x_label)
                plt.savefig('tmp\image' + str(no_of_graphs) + '.png')
                
            def create_scatterplot(col1, col2):
                x_label = col1[0]
                x_values = col1[1:]
                y_label = col2[0]
                y_values = col2[1:]
                global no_of_graphs
                no_of_graphs += 1
                #b,m = polyfit(x_values, y_values, 1)
                plt.scatter(x_values, y_values)
                #plt.plot(x_values, b + m*x_values)
                plt.xlabel(x_label)
                plt.ylabel(y_label)
                plt.savefig('tmp\image' + str(no_of_graphs) + '.png')

            #decisionmaker

            def ca(col):
                #column analysis
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
                    list_types.append(ca(col))
                print(list_types)

            def decisionmaker(list_by_col, list_by_row):
                cols_num = len(list_by_col)
                global no_of_graphs
                no_of_graphs = 0
                if cols_num == 1:
                    if ca(list_by_col[0]) == "ints" or "floats":
                        col = list_by_col[0]
                        col.insert(0, list_by_row[0][0])
                        create_histogram(col)
                    elif ca(list_by_col[0]) == "strings":
                        col = list_by_col[0]
                        col.insert(0, list_by_row[0][0]) 
                        create_bargraph(col)
                    else:
                        print("whooops")

                elif cols_num == 2:
                    # first numbers, second text
                    if (ca(list_by_col[0]) == "ints" or "floats" and ca(list_by_col[1]) == "strings"):
                        col1 = list_by_col[1]
                        col1.insert(0, list_by_row[0][1])
                        col2 = list_by_col[0]
                        col2.insert(0, list_by_row[0][0])
                        cleartmp()
                        plt.clf()
                        create_bargraph_two(col1, col2)
                    # first text, second numbers
                    elif (ca(list_by_col[1]) == "ints" or "floats" and ca(list_by_col[0]) == "strings"):
                        col1 = list_by_col[0]
                        col1.insert(0, list_by_row[0][0])
                        col2 = list_by_col[1]
                        col2.insert(0, list_by_row[0][1])
                        cleartmp()
                        plt.clf()
                        create_bargraph_two(col1, col2)
                    # both numbers
                    elif (ca(list_by_col[1]) == "ints" or "floats" and ca(list_by_col[0]) == "ints" or "floats"):
                        col1 = list_by_col[0]
                        col1.insert(0, list_by_row[0][0])
                        col2 = list_by_col[1]
                        col2.insert(0, list_by_row[0][1])
                        cleartmp()
                        plt.clf()
                        create_scatterplot(col1, col2)
                        plt.clf()
                        create_scatterplot(col2, col1)
                    else:
                        print("whoops")
            cleartmp()
            decisionmaker(list_of_lists_as_columns, list_of_lists_as_rows)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def log_message(self, format, *args):
        return

with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
print("f")

