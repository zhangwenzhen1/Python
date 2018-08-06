import numpy as np
import pandas as pd
        #读取告警表和工参表
alarm = pd.read_csv('D:\guangdong\larm_enodeb.csv',encoding='gbk')
reference = pd.read_csv('D:\guangdong\cfg_enodeb.csv',encoding='gbk')
print(alarm.head())
print(reference.head())
        #告警表匹配厂家
new_alarm = pd.merge(alarm,reference,on='基站ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
print(new_alarm.columns)
new_alarm.drop( axis =1, columns = ['所属地市_y','网管采集经度', '网管采集纬度'], inplace=True)
        #调整列顺序
new_alarm = new_alarm[['所属地市', '设备厂家','基站ID', '基站名称', '告警标题', '告警发生时间', '告警消除时间', '告警状态', '网管告警ID',
       '告警标准名', '网元状态']]
print(new_alarm.columns)
# 查看alarm与new_alarm行数是否一致
print(alarm.iloc[:,0].size)
print(new_alarm.iloc[:,0].size)
# print df.columns.size#列数 2
# print df.iloc[:,0].size#行数 3