import csv
import getdistance
filename = 'D:/湛江.csv'
#file3 = csv.writer(open("output.csv", "w"))
with open(filename) as f:
    reader = csv.reader(f)
    reader1 = list(reader)