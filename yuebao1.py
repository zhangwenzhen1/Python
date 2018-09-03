import pandas as pd
import os
import numpy as np
gc_1=pd.read_csv('D:\guangdong\gc1.csv',encoding='gbk')
gc_2=pd.read_csv('D:\guangdong\gc2.csv',encoding='gbk')
gc=gc_1.append(gc_2)
wyzt_1 = pd.read_csv('D:\guangdong\wyzt_1.csv',encoding='gbk')
wyzt_2 = pd.read_csv('D:\guangdong\wyzt_2.csv',encoding='gbk')
rl=pd.read_csv('D:\guangdong\zhoumangshi0727-0802.csv',encoding='gbk')
wyzt = wyzt_1.append(wyzt_2)
wyzt = wyzt.drop_duplicates('CGI')
wyzt.columns=['小区ID','网元状态']
zb = pd.merge(rl,wyzt,on='小区ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
zb = pd.merge(zb,gc,on='小区ID',how='left',suffixes=('', '_y')) # pandas csv表左连接
zb =zb[['地市', '小区ID', '小区名称', '基站ID', '基站名称', '覆盖场景', '频段', '载频个数', '载波带宽(MHZ)',
       '经度', '纬度', '方位角', '有效RRC连接平均数', '有效RRC连接最大数', 'RRC连接平均数', 'RRC连接最大数',
       '下行PRB平均利用率(v2.8)', '上行PRB平均利用率(v2.8)', 'PDCCH信道CCE占用率', '下行业务信道流量(MB)',
       '上行业务信道流量(MB)', '无线接通率', '上行日流量(MB)', '下行日流量(MB)', '无线掉线率', 'E-RAB掉线率',
       'E-RAB建立成功率', '切换成功率', '网格', '路测网格', '网元状态', ]]
# print(zb.columns)
# print(zb.iloc[:,0].size)
zb = zb.loc[(zb['网元状态']=='现网有业务')]
# print(zb.columns)
# print(zb.iloc[:,0].size)
zb=zb.drop_duplicates('小区ID')
              #计算日流量
zb['日流量GB']=(zb['上行日流量(MB)']+zb['下行日流量(MB)'])/1024
              ##计算单小区日均流量
zb1= zb.groupby('地市',)['日流量GB'].agg(np.mean)
zb1.columns=['地市','单小区日均流量GB']
z_mean=zb['日流量GB'].mean()
zb['单小区日均流量GB'] = zb['地市'].map(zb1)
zb['流量系数']=zb['日流量GB']/zb['单小区日均流量GB']
# print(zb.iloc[:,0].size)
def xishu(a,b):
     if a == 10:
         b = b*2
     if a ==15:
         b = b*20/15
     if a ==5:
         b = b*4
     else:
         b=b
         return b
zb['流量系数'] = zb.apply(lambda x: xishu(x['载波带宽(MHZ)'],x['流量系数']),axis=1)
# print(zb.columns)
# print(zb.iloc[:,0].size)
def f(x):
    return x.max()
zb['最大利用率']=zb[['上行PRB平均利用率(v2.8)','下行PRB平均利用率(v2.8)','PDCCH信道CCE占用率']].apply(f,axis =1)
zb.to_csv('D:\guangdong\liuliangxishu0727-0802.csv',header=1,encoding='gbk')

g1 = zb.loc[(zb['日流量GB']==0) & (zb['地市'].notnull()), ['地市','小区ID','流量系数']]
g2 = zb.loc[(zb['流量系数'] >0) & (zb['流量系数'] <=0.05) , ['地市','小区ID','流量系数']]
g3 = zb.loc[(zb['流量系数'] >0.05) & (zb['流量系数'] <=0.2), ['地市','小区ID','流量系数']]
g4 = zb.loc[(zb['流量系数'] >0.2) & (zb['流量系数'] <=0.5), ['地市','小区ID','流量系数']]
g5 = zb.loc[(zb['流量系数'] >0.5) & (zb['流量系数'] <=1.5), ['地市','小区ID','流量系数']]
g6 = zb.loc[(zb['流量系数'] >1.5) & (zb['流量系数'] <=3), ['地市','小区ID','流量系数']]
g7 = zb.loc[(zb['流量系数'] >3) & (zb['流量系数'] <=5), ['地市','小区ID','流量系数']]
g8 = zb.loc[(zb['流量系数'] >5), ['地市','小区ID','流量系数']]
    #######全省小区系数分布
xishufenbu={'日流量为0':g1['小区ID'].count(),'<=0.05':g2['小区ID'].count(),'0.05~0.2':g3['小区ID'].count(),'0.2~0.5':g4['小区ID'].count(),
            '0.5~1.5':g5['小区ID'].count(),'1.5~3':g6['小区ID'].count(),'3~5':g7['小区ID'].count(),'>5':g8['小区ID'].count()}
xishufenbu=pd.DataFrame(xishufenbu,index=[0])
xishufenbu.to_csv('D:\guangdong\quanshenxishufenbu.csv',header=1,encoding='gbk')
print(xishufenbu)
# xishufenbu=xishufenbu.to_frame()
# print(type(xishufenbu))
g_1 = g1.groupby('地市')['小区ID'].count()
g_2 = g2.groupby('地市')['小区ID'].count()
# print(type(g_2))
# print(g_2.head(30))
g_3 = g3.groupby('地市')['小区ID'].count()
g_4 = g4.groupby('地市')['小区ID'].count()
g_5 = g5.groupby('地市')['小区ID'].count()
g_6 = g6.groupby('地市')['小区ID'].count()
g_7 = g7.groupby('地市')['小区ID'].count()
g_8 = g8.groupby('地市')['小区ID'].count()
# series转换成frame格式
g_1 = g_1.to_frame()
g_2 = g_2.to_frame()
g_2.columns=['流量系数大于0小于0.05的小区数']
# print(g_2.head(30))
g_3 = g_3.to_frame()
g_3.columns=['流量系数大于0.05小于0.2的小区数']
# print(g_3.head(30))
g_4 = g_4.to_frame()
g_5 = g_5.to_frame()
g_6 = g_6.to_frame()
g_7 = g_7.to_frame()
g_8 = g_8.to_frame()
gg = pd.merge(g_1,g_2,on='地市',how='right',suffixes=('', '_y'))
gg = pd.merge(gg,g_3,on='地市',how='left',suffixes=('', '_y')) # pandas csv表左连接
gg = pd.merge(gg,g_4,on='地市',how='left',suffixes=('', '_q'))
gg = pd.merge(gg,g_5,on='地市',how='left',suffixes=('', '_y'))
gg = pd.merge(gg,g_6,on='地市',how='left',suffixes=('', '_y'))
gg = pd.merge(gg,g_7,on='地市',how='left',suffixes=('', '_y'))
gg = pd.merge(gg,g_8,on='地市',how='left',suffixes=('', '_y'))
gg.columns=['日流量为0','流量系数大于0小于0.05的小区数','流量系数大于0.05小于0.2的小区数','流量系数0.2~0.5','流量系数0.5~1.5','流量系数1.5~3','流量系数3~5','流量系数>5']
gg.fillna(0,inplace = True)
gg.loc['全省'] = gg.apply(lambda x: x.sum())
gg['业务均衡比']=(gg['流量系数0.2~0.5']+gg['流量系数0.5~1.5']+gg['流量系数1.5~3'])*1.0/(gg['日流量为0']+gg['流量系数大于0小于0.05的小区数']+gg['流量系数大于0.05小于0.2的小区数']
                +gg['流量系数0.2~0.5']+gg['流量系数0.5~1.5']+gg['流量系数1.5~3']+gg['流量系数3~5']+gg['流量系数>5'])
zb1 = zb1.to_frame()
gg = pd.merge(zb1,gg,on='地市',how='right',suffixes=('', '_y'))
#赋予全省日均流量值
gg.iat[21,0]=z_mean
# print(gg.head(22))
gg=gg.reindex(['全省','广州','深圳','东莞','佛山','汕头','珠海','惠州','中山','江门','湛江','茂名','揭阳','韶关','河源','梅州','汕尾','阳江','肇庆','清远','潮州','云浮'])
gg=gg[['日流量GB','业务均衡比','日流量为0','流量系数大于0小于0.05的小区数','流量系数大于0.05小于0.2的小区数','流量系数0.2~0.5','流量系数0.5~1.5','流量系数1.5~3','流量系数3~5','流量系数>5']]
gg.to_csv('D:\guangdong\junhengbi.csv',header=1,encoding='gbk') #保存列名存储
        #####网格业务均衡统计
# w1 = zb.loc[(zb['流量系数'].isnull())|(zb['流量系数']<=0.2) , ['网格','小区ID','流量系数']]
w1 = zb.loc[(zb['日流量GB']==0) & (zb['地市'].notnull()), ['网格','小区ID','流量系数']]
w2 = zb.loc[(zb['流量系数'] >0) & (zb['流量系数'] <=0.05) , ['网格','小区ID','流量系数']]
w3 = zb.loc[(zb['流量系数'] >0.05) & (zb['流量系数'] <=0.2), ['网格','小区ID','流量系数']]
w4 = zb.loc[(zb['流量系数'] >0.2) & (zb['流量系数'] <=0.5), ['网格','小区ID','流量系数']]
w5 = zb.loc[(zb['流量系数'] >0.5) & (zb['流量系数'] <=1.5), ['网格','小区ID','流量系数']]
w6 = zb.loc[(zb['流量系数'] >1.5) & (zb['流量系数'] <=3), ['网格','小区ID','流量系数']]
w7 = zb.loc[(zb['流量系数'] >3) & (zb['流量系数'] <=5), ['网格','小区ID','流量系数']]
w8 = zb.loc[(zb['流量系数'] >5), ['网格','小区ID','流量系数']]

# w1 = zb.loc[(zb['流量系数']<=0.2) , ['网格','小区ID','流量系数']]
# w2 = zb.loc[(zb['流量系数']>0.2) & (zb['流量系数']<=3) , ['网格','小区ID','流量系数']]
# w3 = zb.loc[(zb['流量系数']>3) , ['网格','小区ID','流量系数']]
w_1 = w1.groupby('网格')['小区ID'].count()
w_2 = w2.groupby('网格')['小区ID'].count()
w_3 = w3.groupby('网格')['小区ID'].count()
w_4 = w4.groupby('网格')['小区ID'].count()
w_5 = w5.groupby('网格')['小区ID'].count()
w_6 = w6.groupby('网格')['小区ID'].count()
w_7 = w7.groupby('网格')['小区ID'].count()
w_8 = w8.groupby('网格')['小区ID'].count()
w_1 = w_1.to_frame()
w_2 = w_2.to_frame()
w_3 = w_3.to_frame()
w_4 = w_4.to_frame()
w_5 = w_5.to_frame()
w_6 = w_6.to_frame()
w_7 = w_7.to_frame()
w_8 = w_8.to_frame()

wg = pd.merge(w_1,w_2,on='网格',how='right',suffixes=('', '_y'))
wg = pd.merge(wg,w_3,on='网格',how='right',suffixes=('', '_y'))
wg = pd.merge(wg,w_4,on='网格',how='right',suffixes=('', '_y'))
wg = pd.merge(wg,w_5,on='网格',how='right',suffixes=('', '_y'))
wg = pd.merge(wg,w_6,on='网格',how='right',suffixes=('', '_y'))
wg = pd.merge(wg,w_7,on='网格',how='right',suffixes=('', '_y'))
wg = pd.merge(wg,w_8,on='网格',how='right',suffixes=('', '_y'))

wg.columns=['日流量为0','流量系数大于0小于0.05的小区数','流量系数大于0.05小于0.2的小区数','流量系数0.2~0.5','流量系数0.5~1.5','流量系数1.5~3','流量系数3~5','流量系数>5']
wg.fillna(0,inplace = True)
wg['总小区数'] = wg['日流量为0']+wg['流量系数大于0小于0.05的小区数']+wg['流量系数大于0.05小于0.2的小区数']+wg['流量系数0.2~0.5']+wg['流量系数0.5~1.5']+wg['流量系数1.5~3']+wg['流量系数3~5']+wg['流量系数>5']
wg['网格业务均衡比'] = (wg['流量系数0.2~0.5']+wg['流量系数0.5~1.5']+wg['流量系数1.5~3'])*1.0/(wg['日流量为0']+wg['流量系数大于0小于0.05的小区数']+wg['流量系数大于0.05小于0.2的小区数']+wg['流量系数0.2~0.5']+wg['流量系数0.5~1.5']+wg['流量系数1.5~3']+wg['流量系数3~5']+wg['流量系数>5'])
# wg['流量系数<=0.2小区占比'] = wg['流量系数<=0.2']*1.0/(wg['流量系数<=0.2']+wg['流量系数0.2<&<=3']+wg['流量系数>3'])
# wg['流量系数0.2<&<=3小区占比'] = wg['流量系数0.2<&<=3']*1.0/(wg['流量系数<=0.2']+wg['流量系数0.2<&<=3']+wg['流量系数>3'])
# wg['流量系数>3小区占比'] = wg['流量系数>3']*1.0/(wg['流量系数<=0.2']+wg['流量系数0.2<&<=3']+wg['流量系数>3'])
wg=wg[['总小区数','网格业务均衡比','日流量为0','流量系数大于0小于0.05的小区数','流量系数大于0.05小于0.2的小区数','流量系数0.2~0.5','流量系数0.5~1.5','流量系数1.5~3','流量系数3~5','流量系数>5']]
# print(wg.head(10))
# wg.reindex(['广州','深圳','东莞','佛山','汕头','珠海','惠州','中山','江门','湛江','茂名','揭阳','韶关','河源','梅州','汕尾','阳江','肇庆','清远','潮州','云浮'])
wg.to_csv('D:\guangdong\wanggejunhengbi.csv',header=1,encoding='gbk') #保存列名存储
        ######高负荷扩容小区统计
gf = pd.read_csv('D:\guangdong\changqigaofuhexiaoqu.csv',encoding='gbk')
gfq = pd.merge(gf,zb,on='小区ID',how='left',suffixes=('', '_y'))
gfq.drop( axis =1, columns= ['地市_y'],inplace=True)
gfq.to_csv('D:\guangdong\gaofuhqd.csv',header=1,encoding='gbk') #保存列名存储
zb_temp = zb[['地市','小区ID','频段','载波带宽(MHZ)','RRC连接最大数']]
gf = pd.merge(gf,zb_temp,on='小区ID',how='left',suffixes=('', '_y'))
gf.drop( axis =1, columns= ['地市_y'],inplace=True)
# print(gf.iloc[:,0].size)
# print(gf.head(20))
###计算长期高负荷各地市小区数
gf1 = gf.loc[( gf['频段'].notnull() | gf['频段'].isnull()) , ['地市', '小区ID', '频段', '载波带宽(MHZ)', 'RRC连接最大数']]
###计算长期高负荷各地市小区数，当RRC连接最大数大于150时
gf6 = gf.loc[(gf['RRC连接最大数']>150) , ['地市','小区ID','频段','载波带宽(MHZ)','RRC连接最大数']]
gf2 = gf.loc[(gf['频段']=='D') , ['地市','小区ID','频段','载波带宽(MHZ)','RRC连接最大数']]
gf3 = gf.loc[(gf['频段']=='E') , ['地市','小区ID','频段','载波带宽(MHZ)','RRC连接最大数']]
gf4 = gf.loc[(gf['频段']=='F') & (gf['载波带宽(MHZ)']==20.0) , ['地市','小区ID','频段','载波带宽(MHZ)','RRC连接最大数']]
gf5 = gf.loc[(gf['频段']=='F') & (gf['载波带宽(MHZ)']==10.0) , ['地市','小区ID','频段','载波带宽(MHZ)','RRC连接最大数']]
gf_1 = gf1.groupby('地市')['小区ID'].count()
gf_2 = gf2.groupby('地市')['小区ID'].count()
gf_3 = gf3.groupby('地市')['小区ID'].count()
gf_4 = gf4.groupby('地市')['小区ID'].count()
gf_5 = gf5.groupby('地市')['小区ID'].count()
gf_6 = gf6.groupby('地市')['小区ID'].count()
gf_1 = gf_1.to_frame()
gf_6 = gf_6.to_frame()
gf_2 = gf_2.to_frame()
gf_3 = gf_3.to_frame()
gf_4 = gf_4.to_frame()
gf_5 = gf_5.to_frame()
gff = pd.merge(gf_1,gf_6,on = '地市',how='left',suffixes=('', '_y'))
gff = pd.merge(gff,gf_2,on = '地市',how='left',suffixes=('', '_y'))
gff = pd.merge(gff,gf_3,on = '地市',how='left',suffixes=('', '_y'))
gff = pd.merge(gff,gf_4,on = '地市',how='left',suffixes=('', '_y'))
gff = pd.merge(gff,gf_5,on = '地市',how='left',suffixes=('', '_y'))
gff.columns = ['长期高负荷小区数','超高用户小区数','D频段小区数','E频段小区数','F1频段小区数','F2频段小区数']
gff.fillna(0,inplace = True)
gff.loc['全省'] = gff.apply(lambda y: y.sum())
gff['超高用户小区数占比'] = gff['超高用户小区数']*1.0/gff['长期高负荷小区数']
gff=gff.reindex(['全省','广州','深圳','东莞','佛山','汕头','珠海','惠州','中山','江门','湛江','茂名','揭阳','韶关','河源','梅州','汕尾','阳江','肇庆','清远','潮州','云浮'])
gff=gff[['长期高负荷小区数','超高用户小区数','超高用户小区数占比','D频段小区数','E频段小区数','F1频段小区数','F2频段小区数']]
gff.to_csv('D:\guangdong\gaofuhetongji.csv',header=1,encoding='gbk') #保存列名存储
        #########地市网格级流量情况#####
zb['路测网格'].fillna('D',inplace = True)
def function(x):
    x=str(x)
    if x.startswith('A'):
        return 'A'
    if x.startswith('C'):
        return 'C'
    if x.startswith('D'):
        return 'D'
    else:
        return 'B'
zb['路测网格']=zb['路测网格'].apply(lambda x: function(x))
wq1 = zb.loc[(zb['路测网格']=='A') , ['地市','小区ID','日流量GB']]
wq2 = zb.loc[(zb['路测网格']=='B') , ['地市','小区ID','日流量GB']]
wq3 = zb.loc[(zb['路测网格']=='C') , ['地市','小区ID','日流量GB']]
wq_1 = wq1.groupby('地市')['日流量GB'].agg([len,np.sum])
wq_2 = wq2.groupby('地市')['日流量GB'].agg([len,np.sum])
wq_3 = wq3.groupby('地市')['日流量GB'].agg([len,np.sum])
wq = pd.merge(wq_1,wq_2,on = '地市',how='left',suffixes=('', '_y'))
wq = pd.merge(wq,wq_3,on = '地市',how='left',suffixes=('', '_y'))
wq.columns = ['A类网格小区数','A类网格流量','B类网格小区数','B类网格流量','C类网格小区数','C类网格流量']
wq.loc['全省'] = wq.apply(lambda y: y.sum())
wq['A类网格流量占比'] = wq['A类网格流量']*1.0/(wq['A类网格流量']+wq['B类网格流量']+wq['C类网格流量'])
wq['B类网格流量占比'] = wq['B类网格流量']*1.0/(wq['A类网格流量']+wq['B类网格流量']+wq['C类网格流量'])
wq['C类网格流量占比'] = wq['C类网格流量']*1.0/(wq['A类网格流量']+wq['B类网格流量']+wq['C类网格流量'])
wq['A类网格小区数占比'] = wq['A类网格小区数']*1.0/(wq['A类网格小区数']+wq['B类网格小区数']+wq['C类网格小区数'])
wq['B类网格小区数占比'] = wq['B类网格小区数']*1.0/(wq['A类网格小区数']+wq['B类网格小区数']+wq['C类网格小区数'])
wq['C类网格小区数占比'] = wq['C类网格小区数']*1.0/(wq['A类网格小区数']+wq['B类网格小区数']+wq['C类网格小区数'])
wq=wq.reindex(['全省','广州','深圳','东莞','佛山','汕头','珠海','惠州','中山','江门','湛江','茂名','揭阳','韶关','河源','梅州','汕尾','阳江','肇庆','清远','潮州','云浮'])
wq.to_csv('D:\guangdong\dishiwanggeliuliangqingku.csv',header=1,encoding='gbk') #保存列名存储