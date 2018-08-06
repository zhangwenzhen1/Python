# encoding=utf8
import fileinput
import os
from math import sin, asin, cos, radians, fabs, sqrt

#输入文件路径
input_file = "D:\Test\zhanjiang.csv"
#输出文件路径
output_file = "D:\Test\output1.csv"

#经纬度、pci等字段所在csv文件的下标，起始下标为0
lon_index = 4
lat_index = 5
azimuth_index = 6

#csv文件存储的字段
data_dict = {}

def init():
    #先将输入的csv文件，按行读取，写入字典中
    for line in fileinput.input(input_file):
        data_dict[line] = "0";

    #结果文件如果存在，先删除之
    if os.path.exists(output_file):
        os.remove(output_file)

def processor():
    #小区编号，累加
    cell_id = 0
    for key in data_dict.keys():
        #如果此行已经处理过，跳出循环
        if data_dict.get(key) != "0":
            continue

        #按分隔符切割字符串，存放在数组中
        arr = key.split(",");

        #提取经纬度以及pci字段的数据
        lon1 = float(arr[lon_index])
        lat1 = float(arr[lat_index])
        azimuth1 = int(arr[azimuth_index])

        #小区编号先自加
        cell_id += 1

        #将此行数据标记为已处理
        data_dict[key] = key.replace("\n", "") + "," + str(cell_id)

        #写入到结果文件中
        output(data_dict.get(key))

        #遍历字典
        for line in data_dict.keys():
            #如果此行已经处理过，跳出循环
            if data_dict[line] != "0":
                continue

            #按分隔符切割字符串，存放在数组中
            jrr = line.split(",");

            #按分隔符切割字符串，存放在数组中
            lon2 = float(jrr[lon_index])
            lat2 = float(jrr[lat_index])
            azimuth2 = int(jrr[azimuth_index])

            #距离小于50米，则标记为已处理，同时写出到文件中
            if get_distance_hav(lon1, lat1, lon2, lat2) < 0.05 and abs(azimuth2-azimuth1)<=10:
                    data_dict[line] = line.replace("\n", "") + "," + str(cell_id)
                    output(data_dict.get(line))


EARTH_RADIUS = 6371  # 地球平均半径，6371km

def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))
    return distance


#写文件
def output(value):
    file_object = open(output_file, 'a')
    file_object.write(value + '\n')
    file_object.close()

#程序执行入口
def process():
    init()
    processor()


process()