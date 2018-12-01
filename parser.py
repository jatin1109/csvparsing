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

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()

while(path==""):
    try:
        file = csv.reader(open(path))
    except:
        path=""
        break

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