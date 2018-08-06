import pandas as pd
import os
import numpy as np
gc_1=pd.read_csv('D:\guangdong\gc1.csv',encoding='gbk')
gc_2=pd.read_csv('D:\guangdong\gc2.csv',encoding='gbk')
gc=gc_1.append(gc_2)
rl=pd.read_csv('D:\guangdong\zhoumangshi0627-0703.csv',encoding='gbk')
#gc.to_csv()--保存
         # 工参表和流量表合并相关字段
zb=pd.merge(rl,gc,on='小区ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
# zb=pd.merge(rl,gc,on='小区ID',left_index=True, right_index=True, how='outer')
# print(zb.columns)
zb=zb[['省份', '地市', '小区ID', '小区名称', '网格', '路测网格','基站ID', '基站名称', '主设备厂家', '室内外基站属性',
       '区域类型', '覆盖场景', '频段', '载频个数', '载波带宽(MHZ)', '经度', '纬度', '方位角',
       '是否属于五期扩容工程', '是否多层网小区', '基础频点小区', '对应的基础频点小区ID', '有效RRC连接平均数',
       '有效RRC连接最大数', 'RRC连接平均数', 'RRC连接最大数', '下行PDSCH PRB占用平均数',
       '下行PDSCH PRB可用平均数', '上行PDSCH PRB占用平均数', '上行PDSCH PRB可用平均数',
       'PDCCH信道CCE可用个数', 'PDCCH信道CCE占用个数', '下行PRB平均利用率(v2.6)',
       '上行PRB平均利用率(v2.6)', '下行PDSCH PRB占用数', '下行PDSCH PRB可用数',
       '上行PDSCH PRB占用数', '上行PDSCH PRB可用数', '下行PRB平均利用率(v2.8)',
       '上行PRB平均利用率(v2.8)', 'PDCCH信道CCE占用率', '下行业务信道流量(MB)', '上行业务信道流量(MB)',
       '下行用户平均速率', '上行用户平均速率', '平均E-RAB数', 'E-RAB建立成功数', 'VOLTE语音话务量',
       'VOLTE语音峰值用户数', '下行VOLTE占用PRB总数', '上行VOLTE占用PRB总数', '分QCI的建立成功次数(QCI5)',
       '小区用户面上行字节数（QCI5）', '小区用户面下行字节数（QCI5）', '无线接通率', 'E-RAB拥塞率(无线资源不足)',
       '上行日流量(MB)', '下行日流量(MB)', '设备型号(仅室外微站填写)', '通道最大发射功率(W)', '无线掉线率',
       '无线掉线率(剔除UI)', 'E-RAB掉线率', 'E-RAB建立成功率', '切换成功率', '天线挂高', 'CQI平均值']]

              #删除重复行
zb=zb.drop_duplicates('小区ID')
              #计算日流量
zb['日流量GB']=(zb['上行日流量(MB)']+zb['下行日流量(MB)'])/1024
# zb.eval("日流量GB=(['上行日流量(MB)']+['下行日流量(MB)'])*1.0/1024",inplace=True)
              ##计算单小区日均流量
zb1= zb.groupby('地市',)['日流量GB'].agg(np.mean)
# zb1.reindex(columns=['地市','单小区日均流量GB'])
# zb1.rename(columns={'地市_x':'地市', '日流量GB':'单小区日均流量GB'}, inplace = True)
zb1.columns=['地市','单小区日均流量GB']
# print(zb1.columns)
# zb1.to_csv('D:\guangdong\meanluliang.csv',header=1,encoding='gbk') #保存列名存储
                     ####计算流量系数
zb['单小区日均流量GB'] = zb['地市'].map(zb1)
zb['流量系数']=zb['日流量GB']/zb['单小区日均流量GB']
# print(zb.head())
# zb.to_csv('D:\guangdong\liuliangxishu.csv',header=1,encoding='gbk')





