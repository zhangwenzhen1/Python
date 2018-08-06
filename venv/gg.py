import csv
import getdistance
#import pandas as pd
def getcodirectionalcell(filename,fileout):
    #filename = 'D:/湛江.csv'
    #fileout = "D:/output.csv"
    lingqu_dict = {}
    f1 = open(fileout,'a')
    biaotou = '地市,CGI,小区名称,方位角,是否满配,共站共向1,共站共向2,共站共向3,共站共向4,共站共向5,共站共向6\n'
    f1.write(biaotou)
    with open(filename) as f:
        reader = csv.reader(f)
        reader1 = list(reader)
        #row_num =2
        for line in reader1:
            lat = line[4]
            lon = line[5]
            name =line[2]#小区名
            #s = int(line[5])%3
            s = int(line[6])
            lili = [line[0],line[1],line[2],line[6],'否']
            #print(line[3])
            for line1 in reader1:
                jat=line1[4]
                jon=line1[5]
                name1=line1[2]
                distance = getdistance.get_distance_hav(float(lon), float(lat), float(jon), float(jat))
                #n=n+1
                #if distance <= 0.05:
                if  name!=name1 and distance<=0.05 and abs(s-int(line1[6]))<=10:
                    lili.append(line1[2])
            if len(lili)>=9:
                lili[4] = '是'
            newline = ','.join(lili)
            f1.write(newline)
            f1.write('\n')
            f1.flush()
            # f.flush()
    f1.close()
    print('complete')

if __name__ =="__main__":
    filename =  'D:/工参数据/湛江12.csv'
    fileout =  'D:/工参数据/zhanjiang12.csv'
    getcodirectionalcell(filename, fileout)










