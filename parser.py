import csv
import numpy as np
import matplotlib.pyplot as plt
import http.server
import socketserver
import re
import urllib.parse

path = ""
PORT = 8080

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
            
            no_of_graphs = 0
            
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
                no_of_graphs += 1
                plt.hist(x_values)
                plt.xlabel(x_label)
                plt.savefig('tmp\image' + no_of_graphs + '.png')

            def create_bargraph(col):
                x_label = col[0]
                x_values1 = col[1:]
                no_of_graphs += 1
                frequency = []
                x_values = []
                for n in x_values1:
                    if n not in x_values:
                        frequency.append(x_values1.count(n))
                        x_values.append(n)
                x_count = len(x_values)
                plt.bar(range(x_count), frequency)
                plt.xlabel(x_values)
                plt.ylabel(x_label)
                plt.savefig('tmp\image' + no_of_graphs + '.png')

            # decisionmaker

            def columnanalyser(col):

                if all(type(i) is int for i in col):
                    return ("ints")
                elif all(type(i) is float for i in col):
                    return ("floats")
                elif all(type(i) is str for i in col):
                    return ("strings")
                else:
                    return ("shit")

            def coltypes(list_by_col):
                list_types = []
                for col in list_by_col:
                    list_types.append(columnanalyser(col))
                print(list_types)

            def decisionmaker(list_by_col, list_by_row):
                cols_num = len(list_by_col)

                if cols_num == 1:
                    if columnanalyser(list_by_col[0]) == "ints" or "floats":
                        col = list_by_col[0]
                        col.insert(0, list_by_row[0][0])
                        create_histogram(col)
                    elif columnanalyser(list_by_col[0]) == "strings":
                        col = list_by_col[0]
                        col.insert(0, list_by_row[0][0]) 
                        create_bargraph(col)
                    else:
                        print("shit")

            decisionmaker(list_of_lists_as_columns, list_of_lists_as_rows)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def log_message(self, format, *args):
        return

with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
print("f")

