import pandas as pd
import numpy as np

def gz(a):
    if 'D' in list(a['基站频段']) and  'F' in list(a['基站频段']):
        a['是否为D+F'] = 'D+F'
        a['是否多载波'] ='D+F共址共向小区'
        return a

    if 'D' in list(a['基站频段']):
        a['是否为D+F'] = '仅有D'
        return a

    if 'F' in list(a['基站频段']):
        a['是否为D+F'] = '仅有F'
        return a

def gz1(b):
    if b['基站频段']=='D' and b['载波数'] >1:
        b['是否多载波'] = 'D频多载波'
        return b

    if b['基站频段']=='D' and b['载波数'] ==1:

        b['是否多载波'] = 'D频单载波'
        return b

    if b['基站频段'] == 'F' and b['载波数'] > 1:
        b['是否多载波'] = 'F频多载波'
        return b

    if b['基站频段'] == 'F' and b['载波数'] == 1:
        b['是否多载波'] = 'F频单载波'
        return b

df = pd.read_csv('D:\Test\output3.csv',encoding='gbk',header=None, names = ['小区名称','基站名称','CGI','责任网格',
                                                                            '基站状态','基站频段','基站经度', '基站纬度',
                                                                            '天线方向角','共站共向标志'])
##建立输出表格式
Fangan = pd.read_csv('D:\Test\zz.csv',encoding='gbk')
###选出含有D，F频的小区
df_temp1 = df.loc[(df['基站频段'] == 'D') |(df['基站频段'] =='F')]
###选出含有E频的小区
df_temp2 = df.loc[(~df['CGI'].isin(df_temp1['CGI']))]
df_temp2['载波数'] =''
df_temp2['是否为D+F'] =''
df_temp2['是否多载波'] =''
df_temp2 =df_temp2[['小区名称','基站名称','CGI','责任网格','基站状态','基站频段','基站经度', '基站纬度','天线方向角',
                '共站共向标志','载波数','是否为D+F','是否多载波',]]
###计算每个频段的载波数量
z = df_temp1.groupby(['共站共向标志','基站频段'])['CGI'].agg(len)
z.columns = ['共站共向标志','基站频段','载波数']
z = z.reset_index(drop=False)
#####在原表df中并入每个频段的载波数量。生成新的表
df_temp1 = pd.merge(df_temp1,z,on=['共站共向标志','基站频段'],how='left',suffixes=('', '_y')) # pandas csv表左连接
df_temp1.columns = ['小区名称','基站名称','CGI','责任网格','基站状态','基站频段','基站经度', '基站纬度','天线方向角',
                    '共站共向标志','载波数']
#######对共站共向小区判断是否为D+F频，是否多载波
i = 1
##判断每组共站共向小区是否为D+F频，是否多载波
while i<= df_temp1['共站共向标志'].max():
    # 选出共站共向基站
    if i in df_temp1['共站共向标志']:
        df_temp = df_temp1.loc[(df_temp1['共站共向标志'] == i)]
        df_temp3 = gz(df_temp)
    Fangan =Fangan.append(df_temp3)
    i+=1
Fangan =Fangan[['小区名称','基站名称','CGI','责任网格','基站状态','基站频段','基站经度', '基站纬度','天线方向角',
                '共站共向标志','载波数','是否为D+F','是否多载波',]]

Fangan_temp1 = Fangan.loc[(Fangan['是否多载波'].isnull())]
Fangan_temp2 = Fangan.loc[(~Fangan['CGI'].isin(Fangan_temp1['CGI']))]
Fangan_temp1 = Fangan_temp1.apply(lambda x: gz1(x),axis =1)
Fangan_temp2 =Fangan_temp2.append(Fangan_temp1)
Fangan_temp2 =Fangan_temp2.append(df_temp2)
Fangan = Fangan_temp2.sort_values(['共站共向标志'])
Fangan.to_csv('D:\Test\Fangan.csv',header=1,encoding='gbk') #保存列名存储


