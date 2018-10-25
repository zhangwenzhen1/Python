import numpy as np
import pandas as pd

#读表
RngLiang1 = pd.read_csv('D:\gxt\MonthRongliang\ZhouBao_1.csv',encoding='gbk')
RngLiang2 = pd.read_csv('D:\gxt\MonthRongliang\ZhouBao_2.csv',encoding='gbk')
RngLiang3 = pd.read_csv('D:\gxt\MonthRongliang\ZhouBao_3.csv',encoding='gbk')
RngLiang4 = pd.read_csv('D:\gxt\MonthRongliang\ZhouBao_4.csv',encoding='gbk')
RngLiang5 = pd.read_csv('D:\gxt\MonthRongliang\ZhouBao_5.csv',encoding='gbk')
GongCan = pd.read_csv('D:\gxt\MonthRongliang\GongCan.csv',encoding='gbk')
ZJ_GongCan = pd.read_csv('D:\gxt\MonthRongliang\ZJ_GongCan.csv',encoding='gbk')

#增加一列CGI在湛江地市的工参上
ZJ_GongCan['CGI'] = '460-00-' + ZJ_GongCan['lnBtsId'].map(str) +'-'+ZJ_GongCan['lcrid'].map(str)
#取消站名后面的D-NLH和F-NLH等字段
GongCan['物理站名'] = GongCan['基站名称'].apply([lambda x: x[:-5]])
GongCan['物理站名'] = GongCan['物理站名'].astype(np.str)
GongCan['物理站名'] =GongCan['物理站名'].apply(lambda x: x.replace('D', ''))
GongCan['物理站名'] =GongCan['物理站名'].apply(lambda x: x.replace('F', ''))
GongCan['物理站名'] =GongCan['物理站名'].apply(lambda x: x.replace('G', ''))
GongCan['物理站名'] =GongCan['物理站名'].apply(lambda x: x.replace('E', ''))
GongCan['物理站名'] =GongCan['物理站名'].apply(lambda x: x.replace('E', ''))

#合并所有的容量周报
RngLiangALL = RngLiang1.append(RngLiang2).append(RngLiang3).append(RngLiang4).append(RngLiang5)
RngLiangALL_temp = RngLiangALL.loc[(RngLiangALL['是否高负荷小区'] == '是') ]
RngLiangALL_temp1 = RngLiangALL.loc[(RngLiangALL['是否高流量感知小区'] == '是') ]

RngLiangALL_temp1 = RngLiangALL_temp1.groupby('CGI')['是否高流量感知小区'].count()
RngLiangALL_temp1 = RngLiangALL_temp1.reset_index(drop=False)
RngLiangALL_temp1['是否高流量感知小区'] = np.where(RngLiangALL_temp1['是否高流量感知小区']>=2,'是','')
# print(RngLiangALL_temp1.columns)
RngLiangALL_temp1.columns =['CGI','是否高流量感知小区(周)']
RngLiangALL = pd.merge(RngLiangALL,RngLiangALL_temp1,on=['CGI'],how='left',suffixes=('', '_y')) # pandas csv表左连接

RngLiangALL_temp2 = RngLiangALL_temp.groupby('CGI')['是否高负荷小区'].count()
RngLiangALL_temp2 = RngLiangALL_temp2.reset_index(drop=False)
RngLiangALL_temp2['是否高负荷小区'] =np.where(RngLiangALL_temp2['是否高负荷小区']>=2,'是','')
RngLiangALL_temp2.columns =['CGI','是否高负荷小区(周)']
RngLiangALL = pd.merge(RngLiangALL,RngLiangALL_temp2,on=['CGI'],how='left',suffixes=('', '_y')) # pandas csv表左连接
# print(RngLiangALL_temp2.columns)
# print(RngLiangALL_temp2.head())
RngLiangALL = RngLiangALL.drop_duplicates()


#把合并起来的月报每列取平均
RngLiangALL1 = RngLiangALL.groupby(['CGI']).agg(np.mean)
RngLiangALL1 = RngLiangALL1.reset_index(drop=False)  #RngLiangALL1 是删除重复的CGI后的版本
RngLiangALL1 = RngLiangALL1.round(2)

#取工参上需要的信息
RngLiangALL1 = pd.merge(RngLiangALL1,GongCan,on='CGI',how='left',suffixes=('', '_y')) # pandas csv表左连接
RngLiangALL1 = pd.merge(RngLiangALL1,ZJ_GongCan,on='CGI',how='left',suffixes=('', '_y'))
# RngLiangALL1 = RngLiangALL1[['CGI' ,'小区名称','基站名称','物理站名','基站频段','基站状态','覆盖类别','天线方向角','Azimuth']]
RngLiangALL1 = RngLiangALL1[['CGI' ,'小区名称','基站名称','物理站名','基站频段','基站状态','覆盖类别','天线方向角','Azimuth',
                             '天线总下倾角','天线挂高','维护片区','优化网格','网络制式','中心频点','自忙时上行利用率PUSCH',
                             '上行利用率PUSCH','自忙时下行利用率PDSCH', '下行利用率PDSCH','自忙时下行利用率PDCCH',
                             '下行利用率PDCCH','日均流量(GB)' , '自忙时峰值利用率','自忙时有效RRC连接最大数',
                             '有效RRC连接最大数','自忙时RRC连接最大数', 'RRC连接最大数',]]
RngLiangALL1 = pd.merge(RngLiangALL1,RngLiangALL_temp2,on=['CGI'],how='left',suffixes=('', '_y')) # pandas csv表左连接
RngLiangALL1 = pd.merge(RngLiangALL1,RngLiangALL_temp1,on=['CGI'],how='left',suffixes=('', '_y')) # pandas csv表左连接
RngLiangALL1 = RngLiangALL1.drop_duplicates('CGI')
###############
RngLiangALL1['流量系数'] = RngLiangALL1['日均流量(GB)']/RngLiangALL1['日均流量(GB)'].mean()
RngLiangALL1['流量系数分段'] = np.where(((RngLiangALL1['流量系数']<=1) & (RngLiangALL1['自忙时峰值利用率']<= 0.15)),'低流量低利用率',
                                  np.where(((RngLiangALL1['流量系数']<=1) & (RngLiangALL1['自忙时峰值利用率'] >0.15) &(RngLiangALL1['自忙时峰值利用率']< 0.5)),'低流量中利用率',
                                           np.where(((RngLiangALL1['流量系数']<=1) & (RngLiangALL1['自忙时峰值利用率'] >=0.5)),'低流量高利用率',
                                                    np.where(((RngLiangALL1['流量系数']>1) & (RngLiangALL1['流量系数']<3) & (RngLiangALL1['自忙时峰值利用率']<= 0.15)),'中流量低利用率',
                                                             np.where(((RngLiangALL1['流量系数']>1) & (RngLiangALL1['流量系数']<3) & (RngLiangALL1['自忙时峰值利用率']>0.15) &(RngLiangALL1['自忙时峰值利用率']<0.5)),'中流量中利用率',
                                                                      np.where(((RngLiangALL1['流量系数']>1) & (RngLiangALL1['流量系数']<3) & (RngLiangALL1['自忙时峰值利用率']>= 0.5)),'中流量高利用率',
                                                                               np.where(((RngLiangALL1['流量系数']>=3) & (RngLiangALL1['自忙时峰值利用率']<= 0.15)),'高流量低利用率',
                                                                                        np.where(((RngLiangALL1['流量系数']>=3) & (RngLiangALL1['自忙时峰值利用率'] >0.15) &(RngLiangALL1['自忙时峰值利用率']< 0.5)),'高流量中利用率',
                                                                                                 np.where(((RngLiangALL1['流量系数']>=1) & (RngLiangALL1['自忙时峰值利用率'] >=0.5)),'高流量高利用率','')))))))))

RngLiangALL1['基站频段'] = RngLiangALL1['基站频段'].astype(np.str)
RngLiangALL1['基站频段'] =RngLiangALL1['基站频段'].apply(lambda x: x.replace('频段', ''))
RngLiangALL1['Azimuth'] = np.where(RngLiangALL1['Azimuth'].isnull(),RngLiangALL1['天线方向角'],RngLiangALL1['Azimuth'])
#RngLiangALL1['小区详情'] = RngLiangALL1['小区名称'].map(str)+'的日均流量(GB)：'+RngLiangALL1['日均流量(GB)'].map(str)+','+'自忙时峰值利用率（%）：'+RngLiangALL1['自忙时峰值利用率'].map(str)+','+'有效RRC连接最大数:'+RngLiangALL1['有效RRC连接最大数'].map(str)+','+'RRC连接最大数：'+RngLiangALL1['RRC连接最大数'].map(str)
df_temp1 = RngLiangALL1.loc[(RngLiangALL1['基站频段'] == 'D') |(RngLiangALL1['基站频段'] =='F')]
###选出含有E频的小区
df_temp2 = RngLiangALL1.loc[(~RngLiangALL1['CGI'].isin(df_temp1['CGI']))]
df_temp1['Azimuth'] = np.where(df_temp1['Azimuth']=='全向',df_temp1['天线方向角'],df_temp1['Azimuth'])
df_temp1['Azimuth'] = df_temp1['Azimuth'].astype(np.uint)
####同向小区数
S = df_temp1.groupby(['物理站名','Azimuth']).count()
S = S.reset_index(drop=False)
S = S[['物理站名','Azimuth', '基站状态']]
S.columns =['物理站名','Azimuth', '同向小区数']
####同站同频同向数
S1 = df_temp1.groupby(['物理站名','基站频段','Azimuth']).count()
S1 = S1.reset_index(drop=False)
S1 = S1[['物理站名','基站频段','Azimuth', '基站状态']]
S1.columns =['物理站名','基站频段','Azimuth', '同站同频同向数']

#物理站小区数
z1 = df_temp1.groupby(['物理站名']).count()
z1 = z1.reset_index(drop=False)
z1 = z1[['物理站名','基站频段', '基站状态']]
z1.columns =['物理站名','基站频段', '物理站小区数']

#z是同个物理站名，同频段小区的个数。
z = df_temp1.groupby(['物理站名','基站频段']).count()
z = z.reset_index(drop=False)
z = z[['物理站名','基站频段', '基站状态']]
z.columns =['物理站名','基站频段', '同频段小区数']

z = pd.merge(z,z1,on='物理站名',how='left',suffixes=('', '_y')) # pandas csv表左连接

#如果同个物理站的小区个数与同频段的小区数相同，那就是仅有D或仅有F。不同就是D+F共址。
z['是否D+F共址站点'] = np.where(z['物理站小区数']!=z['同频段小区数'],'D+F共址',
                          np.where(z['基站频段']=='D','仅D','仅F'))
df_temp1 = pd.merge(df_temp1,z,on=['物理站名','基站频段'],how='left',suffixes=('', '_y')) # pandas csv表左连接

df_temp1 = pd.merge(df_temp1,S,on=['物理站名','Azimuth'],how='left',suffixes=('', '_y')) # pandas csv表左连接

df_temp1 = pd.merge(df_temp1,S1,on=['物理站名','基站频段','Azimuth'],how='left',suffixes=('', '_y')) # pandas csv表左连接


df_temp1['是否共址共向小区'] = np.where(((df_temp1['是否D+F共址站点']=='仅D')& (df_temp1['同向小区数']==1)),'D频单载波',
                                    np.where(((df_temp1['是否D+F共址站点']=='仅D')& (df_temp1['同向小区数']>1)),'D频多载波',
                                             np.where(((df_temp1['是否D+F共址站点']=='仅F')& (df_temp1['同向小区数']==1)),'F频单载波',
                                                      np.where(((df_temp1['是否D+F共址站点']=='仅F')& (df_temp1['同向小区数']>1)),'F频双载波',
                                                               np.where(((df_temp1['是否D+F共址站点'] == 'D+F共址') & (df_temp1['同向小区数']==df_temp1['同站同频同向数'])), 'D+F共址不共向小区','D+F共址共向小区'
                                                               )))))

df_temp1.to_csv('D:\gxt\RngLiangALL1.csv',header=1,encoding='gbk',index=False)
gg = df_temp1.loc[(df_temp1['流量系数分段'] == '高流量高利用率')]
# print(gg.iloc[:,0].size)

gg_temp = df_temp1.loc[(df_temp1['物理站名'].isin(gg['物理站名']))]
gg_temp1 = gg_temp.loc[(((gg_temp['是否共址共向小区'] == 'D+F共址共向小区') | (gg_temp['是否共址共向小区'] == 'D频多载波') | (gg_temp['是否共址共向小区'] == 'F频双载波')))]
gg_temp2 = gg_temp1.loc[((gg_temp1['流量系数分段'] == '中流量低利用率') | (gg_temp1['流量系数分段'] == '低流量低利用率'))]
gg_temp2 = gg_temp2[['CGI' ,'物理站名','Azimuth',]]

gg = pd.merge(gg,gg_temp2,on=['物理站名','Azimuth'],suffixes=('', '_y')) # pandas csv表左连接
# print(gg.iloc[:,0].size)
gg1 = gg.groupby(by='CGI').apply(lambda x:','.join(x['CGI_y']))
gg1 = gg1.to_frame()
gg1= gg1.reset_index(drop=False)
gg1.columns =['CGI','分担小区']
gg2 = pd.merge(gg1,gg,on=['CGI'],how='left',suffixes=('', '_y')) # pandas csv表左连接
gg2 = gg2.drop_duplicates('CGI')
gg2 =gg2[['CGI', '小区名称', '基站名称', '物理站名', '基站频段', '基站状态', '覆盖类别', '天线方向角',
       'Azimuth', '天线总下倾角', '天线挂高', '维护片区', '优化网格', '网络制式', '中心频点',
       '自忙时上行利用率PUSCH', '上行利用率PUSCH', '自忙时下行利用率PDSCH', '下行利用率PDSCH',
       '自忙时下行利用率PDCCH', '下行利用率PDCCH', '日均流量(GB)', '自忙时峰值利用率', '自忙时有效RRC连接最大数',
       '有效RRC连接最大数', '自忙时RRC连接最大数', 'RRC连接最大数', '是否高负荷小区(周)', '是否高流量感知小区(周)',
       '流量系数', '流量系数分段', '同频段小区数', '物理站小区数','同向小区数', '同站同频同向数', '是否D+F共址站点',
        '是否共址共向小区','分担小区', ]]
print(gg2.columns)
gg2.to_csv('D:\gxt\gg2.csv',header=1,encoding='gbk',)