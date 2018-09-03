import pandas as pd
import numpy as np
def function(a):
    df_temp = a.loc[(a['所属地市'].isnull()), ['位置更新数', 'CGI']]
    split = pd.DataFrame((x.split('-') for x in df_temp['CGI']), index=df_temp.index,
                         columns=['编号1', '编号2', '编号3', '小区码CI'])
    df_temp = pd.merge(df_temp, split, right_index=True, left_index=True, suffixes=('', '_y'))
    df_temp['所属ENODEBID'] = '460' + '-' + '00' + '-' + df_temp['编号3'].map(str)
    df_temp.drop(axis=1, columns=['编号1', '编号2', '编号3'], inplace=True)
    a = a.loc[(a['所属地市'].notnull())]
    df_temp = pd.merge(df_temp, a, on='所属ENODEBID', how='left', suffixes=('', '_y'))  # pandas csv表左连接
    df_temp = df_temp.drop_duplicates('CGI')
    df_temp = df_temp[['位置更新数', 'EUTRANCELL名称', '所属地市', '小区码CI', '所属ENODEBID',
                         '生命周期状态', '工程期数', 'CGI', '状态', '所属规划工单', '网络制式', '优化网格', '所属ENODEB']]
    a = a.append(df_temp)
    a['所属地市'].fillna('NULL', inplace=True)
    a = a[~a['所属地市'].isin(['NULL'])]
    return a

def function1(b):
    df_temp = b.loc[(b['所属地市'].isnull()), ['位置更新数','LAC','CI','CGI']]
    b = b.loc[(b['所属地市'].notnull())]
    df_temp = pd.merge(df_temp,b, on='LAC', how='left', suffixes=('', '_y'))  # pandas csv表左连接
    df_temp = df_temp.drop_duplicates('CGI')
    df_temp = df_temp[['位置更新数','小区名称','所属地市','所属区县','所属BTS','生命周期状态','LAC','CI','CGI','覆盖类型','状态']]
    b = b.append(df_temp)
    b['所属地市'].fillna('NULL', inplace=True)
    b = b[~b['所属地市'].isin(['NULL'])]
    return b


