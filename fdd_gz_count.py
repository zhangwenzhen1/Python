import numpy as np
import pandas as pd
import re

df_temp1 = pd.read_csv('D:\gxt\df_temp1.csv',encoding='gbk')
df_temp1['使用频段'] =df_temp1['使用频段'].apply(lambda x: x.replace('DC', 'FDD1800'))
print(df_temp1.iloc[:,0].size)
#########物理站点频段统计
gg1 = df_temp1.groupby(by='物理站名').apply(lambda x:','.join(x['使用频段']))
gg1 = gg1.to_frame()
gg1= gg1.reset_index(drop=False)
gg1.columns=['物理站名','频段类']
#########################################
###去重
def f(x):
    L = re.split(',', x)
    d = ','.join(list(set(L)))
    return d
# print(type(gg1['频段类']))
gg1['频段类'] = gg1['频段类'].apply(lambda x: f(x))
# gg1.to_csv('D:\gxt\df6.csv',header=1,encoding='gbk') #保存列名存储.to_csv('D:\gxt\df2.csv',header=1,encoding='gbk') #保存列名存储

df = df_temp1.pivot_table(df_temp1,index=['物理站名'],columns=['使用频段'],aggfunc={'CGI':len},margins_name=True,)
df = df.reset_index(drop=False)
gp2 = df.copy(deep=True)
gp2.columns = df.columns.droplevel(0)
gp2.columns =['物理站名','D频段小区数','F频段小区数','FDD1800频段小区数']
gp2.fillna(0,inplace = True)
gp2['物理站小区数'] = gp2['D频段小区数']+gp2['F频段小区数']+gp2['FDD1800频段小区数']
# print(gp2.info())
# gp2.to_csv('D:\gxt\df2.csv',header=1,encoding='gbk') #保存列名存储


gp2['共站情况'] = np.where(gp2['D频段小区数']== gp2['物理站小区数'],'仅D频站点',
                       np.where(gp2['F频段小区数']== gp2['物理站小区数'],'仅F频站点',
                                np.where(gp2['FDD1800频段小区数']== gp2['物理站小区数'],'仅FDD1800频站点',
                                         np.where(((gp2['D频段小区数']+gp2['F频段小区数'])== gp2['物理站小区数']) & (gp2['D频段小区数']!=0) & (gp2['F频段小区数']!=0),'D+F共站',
                                                  np.where(((gp2['D频段小区数']+gp2['FDD1800频段小区数'])== gp2['物理站小区数']) & (gp2['D频段小区数']!=0) & (gp2['FDD1800频段小区数']!=0),'D+FDD共站',
                                                           np.where(((gp2['F频段小区数']+gp2['FDD1800频段小区数'])== gp2['物理站小区数']) & (gp2['F频段小区数']!=0) & (gp2['FDD1800频段小区数']!=0),'F+FDD共站','D+F+FDD共站'))))))
# gp2.to_csv('D:\gxt\df3.csv',header=1,encoding='gbk') #保存列名存储



####同向小区数
S = df_temp1.groupby(['物理站名','方位角']).count()
S = S.reset_index(drop=False)
S = S[['物理站名','方位角', '网元状态']]
S.columns =['物理站名','方位角', '同向小区数']
S.to_csv('D:\gxt\df10.csv',header=1,encoding='gbk') #保存列名存储
####同站同频同向数
S1 = df_temp1.groupby(['物理站名','使用频段','方位角']).count()
S1 = S1.reset_index(drop=False)
S1 = S1[['物理站名','使用频段','方位角', '网元状态']]
S1.columns =['物理站名','使用频段','方位角', '同站同频同向数']


g3 = pd.merge(S1,S,on=['物理站名','方位角'],how='left',suffixes=('', '_y')) # pandas csv表左连接
g3 = pd.merge(g3,gp2,on=['物理站名'],how='left',suffixes=('', '_y')) # pandas csv表左连接
g3 = pd.merge(g3,gg1,on=['物理站名'],how='left',suffixes=('', '_y')) # pandas csv表左连接
# g3.to_csv('D:\gxt\df8.csv',header=1,encoding='gbk') #保存列名存储

g3['是否共址共向小区'] = np.where((g3['共站情况']=='仅D频站点')&(g3['同向小区数']==1),'D频单载波',
                          np.where((g3['共站情况']=='仅D频站点')&(g3['同向小区数']>1),'D频多载波',
                                   np.where((g3['共站情况']=='仅F频站点')&(g3['同向小区数']==1),'F频单载波',
                                            np.where((g3['共站情况']=='仅F频站点')&(g3['同向小区数']>1),'F频双载波',
                                                     np.where((g3['共站情况']=='仅FDD1800频站点')&(g3['同向小区数']==1),'FDD1800频单载波',
                                                              np.where((g3['共站情况']=='仅FDD1800频站点')&(g3['同向小区数']>1),'FDD1800频多载波',
                                                                       np.where((g3['共站情况']=='D+F共站')&(g3['同向小区数']==g3['同站同频同向数']),'D+F共址不共向小区',
                                                                                np.where((g3['共站情况']=='D+F共站')&(g3['同向小区数']!=g3['同站同频同向数']),'D+F共址共向小区',
                                                                                         np.where((g3['共站情况']=='D+FDD共站')&(g3['同向小区数']==g3['同站同频同向数']),'D+FDD共址不共向小区',
                                                                                                  np.where((g3['共站情况']=='D+FDD共站')&(g3['同向小区数']!=g3['同站同频同向数']),'D+FDD共址共向小区',
                                                                                                           np.where((g3['共站情况']=='F+FDD共站')&(g3['同向小区数']==g3['同站同频同向数']),'F+FDD共址不共向小区',
                                                                                                                    np.where((g3['共站情况']=='F+FDD共站')&(g3['同向小区数']!=g3['同站同频同向数']),'F+FDD共址共向小区',
                                                                                                                             np.where((g3['共站情况']=='D+F+FDD共站')&(g3['同向小区数']==g3['同站同频同向数']),'D+F+FDD共址两两不共向小区','待定')))))))))))))


# g3.to_csv('D:\gxt\df9.csv',header=1,encoding='gbk') #保存列名存储
print(g3.iloc[:,0].size)
g3_temp = g3.loc[g3['是否共址共向小区']=='待定']

print(g3_temp.iloc[:,0].size)
g3_temp1 = g3_temp.groupby(by=['物理站名','同向小区数']).apply(lambda x:','.join(x['使用频段']))
gg1_temp = g3_temp1.to_frame()
gg1_temp= gg1_temp.reset_index(drop=False)
gg1_temp.columns=['物理站名','同向小区数','频段类1']
# print(gg1_temp.head())

gg1_temp['频段类1'] = gg1_temp['频段类1'].apply(lambda x: f(x))
gg1_temp['aa'] =np.where(gg1_temp['频段类1']=='D,F','D+F共向，D+F+FDD不共向',
                         np.where(gg1_temp['频段类1']=='D,FDD1800','D+FDD共向，D+F+FDD不共向',
                                  np.where(gg1_temp['频段类1']=='F,FDD1800','F+FDD共向，D+F+FDD不共向','D+F+FDD共向')))

g3_temp= g3_temp.reset_index()

gg1_temp = pd.merge(g3_temp,gg1_temp,on=['物理站名','同向小区数'],how='left',suffixes=('', '_y')) # pandas csv表左连接
# print(gg1_temp.head())
gg1_temp.rename(columns={'index': '序号'},inplace=True)
# print(gg1_temp.head())
gg1_temp =gg1_temp[['序号','aa']]
gg1_temp.set_index('序号',inplace=True)
# print(gg1_temp.head())
result = pd.merge(g3,gg1_temp,right_index=True, left_index=True,how ='outer',suffixes=('', '_y'))
result['是否共址共向小区'] =np.where(result['是否共址共向小区']=='待定',result['aa'],result['是否共址共向小区'])
print(result.iloc[:,0].size)

result.to_csv('D:\gxt\Result.csv',header=1,encoding='gbk') #保存列名存储
print(result.columns)
print(df_temp1.columns)
Result = pd.merge(df_temp1,result,on=['物理站名','使用频段','方位角'],how='left',suffixes=('', '_y')) # pandas csv表左连接
Result.drop( axis =1, columns= ['aa'],inplace=True)
print(Result.iloc[:,0].size)
print(Result.columns)
Result.to_csv('D:\gxt\Result1.csv',header=1,encoding='gbk') #保存列名存储

