import csv
import getdistance
from math import radians, cos, sin, asin, sqrt
file1 = open("D:/性能数据/深圳.csv")
file3 = csv.writer(open("output.csv", "w"))
data_dict = {}
output_dict = {}
for line in file1:
    data_dict[line] = "0"
#for key in data_dict.keys():
for key in data_dict.values():
    print(key)
"""
    arr = key.split(",");
    lon = float(arr[3])
    lat = float(arr[4])
    for jey in data_dict.keys():
        if key == jey:
            continue
        jrr = jey.split(",");
        jon = float(jrr[3])
        jat = float(jrr[4])
        distance = getdistance.get_distance_hav(lon, lat, jon, jat)
"""





