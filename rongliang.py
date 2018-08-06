import csv
import getdistance
#import pandas as pd
filename = 'D:/湛江.csv'
file3 = csv.writer(open("output.csv", "w"))
lingqu_dict = {}
with open(filename) as f:
    reader = csv.reader(f)
    reader1 = list(reader)
    row_num =2
    #print(reader1[row_num])
    while row_num < len(reader1)-1:
        lat = reader1[row_num][3]
        lon = reader1[row_num][4]
        #print(lat, lon)
        row1_num = row_num+1
        n=0
        while row1_num < len(reader1):
            jat = reader1[row1_num][3]
            jon = reader1[row1_num][4]
            distance = getdistance.get_distance_hav(float(lon), float(lat), float(jon), float(jat))

            #print(distance)
            if distance<= 0.05:
                 lingqu_dict.setdefault(reader1[row_num][1], []).append(reader1[row1_num][1])
                 n=n+1
            row1_num += 1
        row_num+=1
        print(n)





    #print(lat, lon)

    #print(list(reader)[1])
    # for item in reader:
    #    # print(item)
    #     lat = float(item[2])
    #     lon = float(item[3])
    #     #print(lat,lon)
     #   for item1 in reader:
       #     jat=float(item)








    # 读取一行，下面的reader中已经没有该行了
    # head_row = next(reader)
    # print(head_row)

"""
with open(filename) as f:
    reader = csv.DictReader(f)
   for row in reader:
        # Max TemperatureF是表第一行的某个数据，作为key
        max_temp = row['所属地市']
        print(max_temp)
    len(row['所属地市'])
    print() 
"""

