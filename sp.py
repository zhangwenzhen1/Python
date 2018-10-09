import pandas as pd
import numpy as np
from math import sin, asin, cos, radians, fabs, sqrt

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


def match_distance_degree(arr):
    temp["经度"] = arr["基站经度"]
    temp["纬度"] = arr["基站纬度"]

    EARTH_REDIUS = 6371
    lonA = np.radians(temp["经度"])
    latA = np.radians(temp["纬度"])
    lonB = np.radians(temp["基站经度"])
    latB = np.radians(temp["基站纬度"])

    # 利用haversine公式计算两个经纬度之间的距离(单位：千米)
    a = latA - latB  # 两点纬度之差
    b = lonA - lonB  # 两点经度之差
    distance = 2 * np.arcsin(
        np.sqrt(np.sin(a / 2) ** 2 + np.cos(latA) * np.cos(latB) * np.sin(b / 2) ** 2)) * EARTH_REDIUS
    temp["距离(m)"] = distance * 1000

    # 两个经纬度连线的方位角
    dlon = lonB - lonA
    y = np.sin(dlon) * np.cos(latB)
    x = np.cos(latA) * np.sin(latB) - np.sin(latA) * np.cos(latB) * np.cos(dlon)
    brng = np.degrees(np.arctan2(y, x))
    brng = (brng + 360) % 360
    degree = brng - temp["天线方向角"]
    temp["夹角"] = degree


def zz(a,b) :

   while i< len(b):
       if  b.iat[i,1] <a <b.iat[i,2]:
           return b.iat[i,3]
       i+=1



######读取表
df = pd.read_csv('D:\Test\gc0913.csv',encoding='gbk')
df = df[[ '小区名称','基站名称','CGI','责任网格','基站状态','基站频段','基站经度', '基站纬度','天线方向角']]
df = df.loc[(df['基站状态'] == '现网有业务') & (df['基站经度'].notnull()) &(df['基站纬度'].notnull()) & (df['基站频段'].isin(['D频段','F频段','E频段']))]
df['基站频段'] = df['基站频段'].apply(lambda x: x.replace('频段', ''))
df = df.drop_duplicates()
# split = pd.DataFrame((x.split('-') for x in df['基站名称']),index=df.index)
df['基站名称'] = df['基站名称'].apply([lambda x: x[:-5]])
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('F-NLH', ''))
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('D-NLH', ''))
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('E-NLH', ''))
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('F-ZLH', ''))
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('E-NLW', ''))
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('D-NLW', ''))
# df['基站名称'] = df['基站名称'].apply(lambda x: x.replace('F-NLW', ''))

df = df.sort_values(['基站名称'])
df = df.reset_index(drop=True)
df['天线方向角'] = df['天线方向角'].astype(np.int)
print(df['基站名称'].head(100))
# df['共站标志'] = 0
# flag = 0
# i = 0
# j = 0
# temp = df.copy()
# df['flag'] =df.apply(match_distance_degree, axis=1)

# while i < len(df['CGI']):
#     # 如果此行已经处理过，跳出循环
#     if df.loc[i,'共站标志'] != 0:
#         continue
#     flag += 1
#     while j < len(df['CGI']):
#         # 如果此行已经处理过，跳出循环
#         if df.loc[j,'共站标志'] != 0:
#             continue
#         if get_distance_hav(df.loc[i,'基站经度'], df.loc[i,'基站纬度'], df.loc[j,'基站经度'], df.loc[j,'基站纬度']) < 0.05:
#             df.loc[j,'共站标志'] = flag
#         j+=1
#     i+=1
# df = df.sort_values(['共站标志'])
#
df.to_csv('D:\Test\zj.csv',header=1,encoding='gbk',index=False) #保存列名存储

