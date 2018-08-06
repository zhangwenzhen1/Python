from gg import getcodirectionalcell
import getdistance
from multiprocessing import Pool,Process
# filename = 'C:/Users/zhanngwenzhen/Desktop/湛江1.csv'
# fileout = "D:/zhanjiang.csv"
filename1 = 'D:/性能数据/潮州.csv'
filename2 = 'D:/性能数据/东莞.csv'
filename3 = 'D:/性能数据/佛山.csv'
filename4 = 'D:/性能数据/广州.csv'
filename5 = 'D:/性能数据/河源.csv'
filename6 = 'D:/性能数据/惠州.csv'
filename7 = 'D:/性能数据/江门.csv'
filename8 = 'D:/性能数据/揭阳.csv'
filename9 = 'D:/性能数据/茂名.csv'
filename10 = 'D:/性能数据/梅州.csv'
filename11 = 'D:/性能数据/清远.csv'
filename12 = 'D:/性能数据/汕头.csv'
filename13 = 'D:/性能数据/汕尾.csv'
filename14 = 'D:/性能数据/韶关.csv'
filename15 = 'D:/性能数据/深圳.csv'
filename16 = 'D:/性能数据/阳江.csv'
filename17 = 'D:/性能数据/云浮.csv'
filename18 = 'D:/性能数据/湛江.csv'
filename19 = 'D:/性能数据/肇庆.csv'
filename20 = 'D:/性能数据/中山.csv'
filename21 = 'D:/性能数据/珠海.csv'
fileout1 ='D:/性能数据/chaozhou.csv'
fileout2 = 'D:/性能数据/dongguan.csv'
fileout3 = 'D:/性能数据/foshan.csv'
fileout4 = 'D:/性能数据/guangzhou.csv'
fileout5 = 'D:/性能数据/heyuan.csv'
fileout6 = 'D:/性能数据/huizhou.csv'
fileout7 = 'D:/性能数据/jiangmen.csv'
fileout8 = 'D:/性能数据/jieyang.csv'
fileout9 = 'D:/性能数据/maoming.csv'
fileout10 = 'D:/性能数据/meizhou.csv'
fileout11 = 'D:/性能数据/qingyuan.csv'
fileout12 = 'D:/性能数据/shantou.csv'
fileout13 = 'D:/性能数据/shanwei.csv'
fileout14 = 'D:/性能数据/shaoguan.csv'
fileout15 = 'D:/性能数据/shenzhen.csv'
fileout16 = 'D:/性能数据/yangjiang.csv'
fileout17 = 'D:/性能数据/yunfu.csv'
fileout18 = 'D:/性能数据/zhanjiang.csv'
fileout19 = 'D:/性能数据/zhaoqing.csv'
fileout20 = 'D:/性能数据/zhongshan.csv'
fileout21 = 'D:/性能数据/zhuhai.csv'
inputlist = [filename1,filename2,filename3,filename4,filename5,filename6,filename7,filename8,filename9,filename10,
            filename11,filename12,filename13,filename14,filename15,filename16,filename17,filename18,filename19,
            filename20,filename21]
outlist = [fileout1,fileout2,fileout3,fileout4,fileout5,fileout6,fileout7,fileout8,fileout9,fileout10,fileout11,
          fileout12,fileout13,fileout14,fileout15,fileout16,fileout17,fileout18,fileout19,fileout20,fileout21]

if __name__ == "__main__":
    pool = Pool(8)
    for i in range(21):
        pool.apply_async(func=getcodirectionalcell,args=(inputlist[i],outlist[i]))
    pool.close()
    pool.join()
