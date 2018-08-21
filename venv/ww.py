import pandas as pd
import os
import numpy as np
df = pd.read_csv('D:\guangdong\Rongliang\g1.csv',encoding='gbk')
Fangan = pd.read_csv('D:\guangdong\Rongliang\g11.csv',encoding='gbk')
# df1 = pd.read_csv('D:\Test\output1.csv',encoding='gbk')
# print(df.iat[0,10])
i=1
def fangan(a):
    if a == 3:
        return '建议扩容'
    if a == 2:
        return '该小区不存在容量问题'
    if a == 1:
        return '建议吸收邻区业务或现场排查'

#按共站共向基站分组
while i<= df['是否共站共向标志'].max():

    # 选出共站共向基站
    df_temp = df.loc[(df['是否共站共向标志'] ==i), ['地市','小区ID','小区名称','室内外基站属性','经度','纬度','方位角',
                                          '是否共站共向标志','流量系数','流量系数分段']].sort_values(['流量系数分段'])
    df_temp =df_temp.sort_values(['流量系数'])
    df_temp['方案']= None
    df_temp = df_temp.reset_index(drop=True)
    df_temp = df_temp.reindex()

    # 统计共站共向小区个数
    j = len(df_temp)
    m = len(df_temp) #小区是否满配的标志
    # 给出无共站共向小区的解决方案
    if j==1 :
        df_temp['方案']= df_temp['流量系数分段'].apply(lambda a: fangan(a))

    else:
        print(df_temp.index)
        # print(j)
        ###处理含有高流量的共站共向小区容量问题
        if j>1 and df_temp.iat[j-1, 9] ==3:# 判断是否为高流量
            # m = j - 1
            while j>1:
                if df_temp.iat[0, 9]==1:# 判断是否为低流量
                    k=1
                    while k<len(df_temp):
                        if df_temp.iat[k, 8]>=3:#流量分段为高流量
                            df_temp.iat[k,10]='可让小区'+str(df_temp.iat[0,1])+'分担容量'
                            df_temp.iat[0,10]='可以分担小区'+str(df_temp.iat[k,1])+'容量'
                        if df_temp.iat[k, 8]>0.2 and df_temp.iat[k, 8]<3:
                            df_temp.iat[k, 10] = '该小区不存在容量问题'
                        if df_temp.iat[k, 9]==1:
                            df_temp.iat[k, 10] = '可以分担小区'+str(df_temp.iat[len(df_temp)-1,1])+'容量'
                        k=k+1
                if df_temp.iat[0, 9] == 2:

                    if df_temp.iat[0, 8]<0.8:
                        k=1
                        while k < len(df_temp):
                            if df_temp.iat[k, 8]>=3:
                                df_temp.iat[k, 10] = '可让小区' + str(df_temp.iat[0, 1]) + '分担容量'
                                df_temp.iat[0, 10] = '可以分担小区' + str(df_temp.iat[k, 1]) + '容量'
                            if df_temp.iat[k, 8]<3:
                                df_temp.iat[k, 10] = '该小区不存在容量问题'
                            k=k+1
                    else:
                        k=1
                        while k < len(df_temp):
                            if df_temp.iat[k, 9]==2:
                                df_temp.iat[k, 10] = '该小区不存在容量问题'
                            else:
                                if m>=5:
                                    df_temp.iat[k, 10] = '建议增加微小站'
                                else:
                                    df_temp.iat[k, 10] = '建议对该小区扩容'

                if df_temp.iat[0,9]==3: # 判断是否为高流量
                    if m>=5:
                        df_temp.iat[0, 10] = '建议增加微小站'
                        k = 1
                        while k < len(df_temp):
                            df_temp.iat[k, 10] = '建议增加微小站'
                            k=k+1
                    else:
                        df_temp.iat[0, 10] = '对该小区扩容'
                        k = 1
                        while k < len(df_temp):
                            df_temp.iat[k, 10] = '对该小区扩容'
                            k = k + 1
                j=j-1
        ###处理不含有高流量的共站共向小区容量问题
        if j > 1 and df_temp.iat[j - 1, 9] == 2:  # 判断是否为中流量

            while j>1:

                if df_temp.iat[0, 9] == 1:  # 判断是否为低流量
                    df_temp.iat[0, 10] = '可以分担小区' + str(df_temp.iat[len(df_temp) - 1, 1]) + '容量'
                    k=1
                    while k < len(df_temp):
                        if df_temp.iat[k, 9]==1:
                            df_temp.iat[k, 10] = '可以分担小区' + str(df_temp.iat[len(df_temp) - 1, 1]) + '容量'
                        else:
                            df_temp.iat[k, 10] = '该小区不存在容量问题'
                        k = k + 1
                else:
                    df_temp.iat[0, 10] = '该小区不存在容量问题'
                    k = 1
                    while k < len(df_temp):
                        df_temp.iat[k, 10] = '该小区不存在容量问题'
                        k=k+1
                j = j - 1
        ###处理只含有低流量的共站共向小区容量问题
        if j > 1 and df_temp.iat[j - 1, 9] == 1:  # 判断是否为低流量
            df_temp.iat[0, 10] = '建议小区减容'
            while j>1:
                df_temp.iat[j - 1, 10] = '建议对共站共向小区' + str(df_temp.iat[0, 1]) + '减容'
                j=j-1
    Fangan = Fangan.append(df_temp)
    # df_temp.columns = ['地市','小区ID','小区名称','室内外基站属性','经度','纬度','方位角','是否共站共向标志','流量系数','流量系数分段','方案']
    i = i+1
print(i)
Fangan.to_csv('D:\guangdong\Rongliang\g12.csv',header=1,encoding='gbk') #保存列名存储 =
# df['A'].shift(1)