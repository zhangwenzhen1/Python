import pandas as pd
import numpy as np
import ty
df  =  pd.read_csv('D:\zhanjiang\Cl2Gcell.csv',encoding='gbk')
df2 = pd.read_csv('D:\zhanjiang\Lcz2Gcell.csv',encoding='gbk')
df4 = pd.read_csv('D:\zhanjiang\Addressupdate2G0824.csv',encoding='gbk')
df4 = df4.drop_duplicates('CGI')
df5 = pd.read_csv('D:\zhanjiang\Addressupdate2G0825.csv',encoding='gbk')
df5 = df5.drop_duplicates('CGI')
df6 = pd.read_csv('D:\zhanjiang\Addressupdate2G0826.csv',encoding='gbk')
df6 = df6.drop_duplicates('CGI')

##2G工参表合并
df = df.append(df2)
df = df.drop_duplicates('CGI')
##2G位置更新表合并
df4 = df4.append(df5)
df4 = df4.append(df6)
df4 = df4.drop_duplicates('CGI')

##2G工参表与位置更新表合并
df4 = pd.merge(df4,df,on='CGI',how='left',suffixes=('', '_y')) # pandas csv表左连接
###选取需要的列
df4 = df4[['位置更新数','小区名称','所属地市','所属区县','所属BTS','生命周期状态','LAC','CI','CGI','覆盖类型','状态']]
#########删除重复行
df4 = df4.drop_duplicates('CGI')
# df4.to_csv('D:\zhanjiang\GSM.csv',header=1,encoding='gbk',index=False) #保存列名存储
df4_temp = ty.function1(df4)
df4_temp.to_csv('D:\zhanjiang\AllGSM.csv',header=1,encoding='gbk',index=False) #保存列名存储
# df4.to_csv('D:\zhanjiang\GSM.csv',header=1,encoding='gbk',index=False) #保存列名存储