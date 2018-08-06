import pandas as pd
import os
import numpy
g=pd.read_csv('D:\guangdong\hh.csv',encoding='gbk')
# g['日流量']=g['上行日流量']+g['下行日流量']
g.eval('日流量=上行日流量+下行日流量',inplace=True)
g1=g.groupby('地市')['日流量'].mean()
# g1=g.set_index('小区名称').groupby('地市')['日流量'].mean()

 # g1= g1.groupby('地市').mean()
print(type(g))
# g['小区名称'].replace(regex=[r'^a.$'], value='A')
def function(x):
    if 'a' in x:
        return 'A'
    if 'b' in x:
        return 'B'
    if 'c' in x:
        return 'C'
    else:
        return 'D'
g['test'] = g['小区名称'].apply(lambda x: function(x))
# 使用apply函数, 如果city字段包含'ing'关键词，则'判断'这一列赋值为1,否则为0
#frame['panduan'] = frame.city.apply(lambda x: 1 if 'ing' in x else 0)
print(g)
'''
    import csv as csv
import numpy as np

# -------------
# csv读取表格数据
# -------------

csv_file_object = csv.reader(codecs.open('ReaderRentRecode.csv', 'rb'))
header = csv_file_object.next()
print header
print type(header)
print header[1]

data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

print data[0::, 0]

# -------------
# pandas读取表格数据
# -------------
import pandas as pd

df = pd.read_csv('ReaderRentRecode.csv')  # 读者借阅信息表

print df.head()
print '----------------'
print df[['读者证号', '读者姓名', '书名', '中图法分类号']]  # 选取其中的四列
print '------------------------------------------------------------------'
print

dd = pd.read_csv('ReaderInformation.csv')

print dd.head()
print '----------------'
print dd[['读者证号', '读者性别', '读者单位', '读者类别']]
print '------------------------------------------------------------------'
print

data = pd.merge(df, dd, on=['读者证号', '读者姓名'], how='left')  # pandas csv表左连接
data = data[['读者证号', '读者姓名', '读者性别', '书名', '中图法分类号', '读者单位', '读者类别']]
print data


# -------------
# pandas写入表格数据
# -------------
data.to_csv(r'data.csv', encoding='gbk')
'''
