import re

fh = open('Ülesanne10.txt')
for line in fh:
    if re.search('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', line):
         print(line,end='')

fh = open('Ülesanne10.txt')
for parool in fh:
    if re.search('^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$', parool):
         print(parool,end='')