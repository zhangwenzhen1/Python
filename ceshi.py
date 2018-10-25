import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
# 显示中文
font1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simkai.ttf')# 显示中文
plt.plot(np.random.randn(50).cumsum(),color ='k',linestyle='dashed',marker ='o')
ax1.hist(np.random.randn(100),bins=20,color ='k',alpha =0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
ax4 = fig.add_subplot(2,2,4)
data =np.random.randn(30).cumsum()
plt.plot(data,color ='g',label='故1')
plt.plot(data,'k--',drawstyle='steps-post',label='设及')
# fig,axes =plt.subplots(2,3)

plt.legend(loc='best',prop=font1)# 显示中文
plt.show()
# sz_1 = pd.read_csv('D:\shenzhen\sz_FDD-46.csv',encoding='gbk')
# sz_2 = pd.read_csv('D:\shenzhen\sz_FDD-73.csv',encoding='gbk')
# shenzhen_CGI = pd.read_csv('D:\shenzhen\szcgi.csv',encoding='gbk')
# sz = sz_1.append(sz_2)
# sz = sz.drop_duplicates()
# # sz = sz.loc[(~sz['CGI'].isin(shenzhen_CGI['CGI']))]
# print(sz.iloc[:,0].size)
# print(sz.columns)