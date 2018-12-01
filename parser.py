import csv
import numpy as np
import matplotlib.pyplot as plt
import http.server
import socketserver
import re


path = ""
PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if(re.match(r'/graph.html.*',self.path) != None):
            path = re.findall(r'(?<=/graph.html\?path=).*', self.path)[0]
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    def log_message(self, format, *args):
        return

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

while(path==""):
    try:
        file = csv.reader(open(path))
    except:
        path=""
        continue

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
        for i in row1:
            if RepresentsInt(i):
                i = float(i)
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

