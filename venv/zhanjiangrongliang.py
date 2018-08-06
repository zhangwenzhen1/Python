import numpy as np
import pandas as pd
        #读流量系数
coefficient = pd.read_csv('D:\zhanjiang\coefficient.csv',encoding='gbk')
        #读共站共向小区
codirectionalcell = pd.read_csv('D:\zhanjiang\codirectionalcell.csv',encoding='gbk')
        #读取切换门限
CP3CIO = pd.read_csv('D:\zhanjiang\CP3CIO.csv',encoding='gbk')
CP4CIO = pd.read_csv('D:\zhanjiang\CP4CIO.csv',encoding='gbk')
        #读取同异频门限
yipinmenxian = pd.read_csv('D:\zhanjiang\yipinmenxian.csv',encoding='gbk')
Tongpinmenxian= pd.read_csv('D:\zhanjiang\Tongpinmenxian.csv',encoding='gbk')
        #分别删除读流量系数和共站共向小区重复小区
coefficient=coefficient.drop_duplicates('小区ID')
codirectionalcell=codirectionalcell.drop_duplicates('小区ID')
# print(coefficient.iloc[:,0].size)
# print(codirectionalcell.iloc[:,0].size)
CP3CIO=CP3CIO.drop_duplicates('小区ID')
CP4CIO=CP4CIO.drop_duplicates('小区ID')
CP=CP3CIO.append(CP4CIO)
        #
new_1 = pd.merge(coefficient,codirectionalcell,on='小区ID',how='right',suffixes=('', '_y')) # pandas csv表左连接
# print(new_1.columns)
new_2=new_1[[ '小区ID', '小区中文名', '方位角', '最小网格', '日流量GB', '最大利用率', '流量系数', '流量系数分段'
    ,'共站共向1', '共站共向2', '共站共向3', '共站共向4', '共站共向5', '共站共向6']]

# def function(a,b,c):
#     if a in b:
#         return c.value()
#
# new_2['test'] = new_2.apply(lambda x: function(x['共站共向1'],x[ '小区中文名'],x['流量系数分段']))
# new2_['']
# print(new_2.columns)
# new_1.loc[(new_1['流量系数分段'] == '低流量'), ['id','city','age','category','gender']]
# zz=new_1.loc[(new_1['流量系数分段'] =='低流量') & (new_1['小区中文名'] for new_1['小区中文名'] in new_2.loc[:,['共站共向1']:['共站共向4']]),[ '小区ID', '小区中文名', '方位角', '最小网格', '日流量GB', '最大利用率', '流量系数', '流量系数分段'
#     ,'共站共向1', '共站共向2', '共站共向3', '共站共向4', '共站共向5', '共站共向6','ww']]
# print(type(zz))
new_3=new_2.loc[new_2['共站共向1'].notnull()]
print(new_3.iloc[:,0].size)
print(new_2.iloc[:,0].size)
# tt=new_2.pop('小区中文名')
# print(tt)
# new_2.insert(9,'流量分段',)
# new_1.loc[new_1['小区中文名']==new_2['共站共向1']]=new_1['流量系数分段']
# print(new_2.columns)
zz = new_2[['小区中文名','流量系数分段']]
# zz.columns=[['共站共向1','流量分段1']]
# zz=new_2.loc[(new_2['共站共向1'] ==' ') , ['小区ID', '小区中文名', '方位角', '最小网格', '日流量GB', '最大利用率', '流量系数', '流量系数分段'
#     ,'共站共向1', '共站共向2', '共站共向3', '共站共向4', '共站共向5', '共站共向6']].sort_values(['小区ID'])
test = pd.merge(new_2,zz,left_on='共站共向1',right_on= '小区中文名',how='left',suffixes=('', '_y')) # pandas csv表左连接
# test1 = pd.merge(new_2,zz,on='共站共向1',how='left',suffixes=('', '_y')) # pandas csv表左连接
print(test.iloc[:,0].size)
# print(test1.iloc[:,0].size)
test1=test.drop_duplicates('小区ID')
print(test1.iloc[:,0].size)
print(zz.iloc[:,0].size)
# test1.to_csv('D:\zhanjiang\est1.csv',header=1,encoding='gbk')

# new_2.to_csv('D:\zhanjiang\Test.csv',header=1,encoding='gbk')
# Test = pd.read_csv('D:\zhanjiang\Test.csv',encoding='gbk')
# Test_1 = pd.merge(Test,CP3CIO,on='小区ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
# Test_1 = pd.merge(Test_1,yipinmenxian,on='小区ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
# Test_1 = pd.merge(Test_1,Tongpinmenxian,on='小区ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
# print(Test_1.columns)
# Test_1.to_csv('D:\zhanjiang\Test_1.csv', header=1, encoding='gbk')