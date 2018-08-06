import fileinput
import csv
input_file = "D:/chaozhou.txt"
for line in fileinput.input(input_file,'rb'):

        print(line)