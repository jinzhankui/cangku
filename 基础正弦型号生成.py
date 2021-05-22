import matplotlib.pyplot as plt
#导入库
import numpy as np
#将numpy重新命名为np
x=np.linspace(0,3*np.pi,100)
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认100
y=np.sin(x)
#定义sin函数
plt.rcParams['font.sans-serif']=['SimHei']#加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)
#是指一个1行2列的图中从左到右从上到下的第一个位置
plt.title(r'$f(x)=sin(x)$')
#在图面上显示sin
plt.plot(x,y)
#画图语句 x为x轴数据，y为y轴数据
plt.show()
#显示图片
x1 = [t*0.375*np.pi for t in x]
#为x1赋值
y1 = np.sin(x1)
#将参数x带入y1
plt.subplot(1,2,2)
#是指一个1行2列的图中从左到右从上到下的第二个位置
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
#显示w
plt.plot(x, y1)
#画图语句 x1为x轴数据，y1为y轴数据
plt.show()
#显示图片