# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/6 12:41
print('——————————range()的使用————————————————')
s=range(10) #是一个整数序列，range(stop),range(start,stop),range(star,stop,step)三种方式
#前两个步长为1，到stop为止，不包含stop,优势是只有使用的时候才会占用内存数据；
print(list(s))
r=range(1,20)#从1开始到19,
print(list(r))

t=range(2,23,2)#从2开始，步长为2，2,4,6,8,10-100；

print(list(t))

print('——————————while循环结构————————————————')
#while循环的使用
#0到100之间的累加和
#0到100之间的偶数和
a=0            #第一步初始化变量
while a<=10:   #第二步条件判断，条件判断和初始化变量平行
    print(a)   #第三步条件执行体
    a+=1       #第四步改变变量 ，和第三部条件执行体平行
#当条件判断为真时执行循环，为假时退出循环
a=0
while a<10:
     a += 1
print(a) #条件判断了N+1次，while执行了N次，输出为11，a=11的时候退出了循环执行print
#也就是当条件判断为False，跳出循环，程序继续往下走

#0到100之间的累加和
a=0
sum1=0
while a<=100:
    if a%2==0:
       sum1+=a
    a+=1
print(sum1)
#0到100之间的奇数累加和
a=0
sum1=0
while a<=100:
    if not a%2==0:
       sum1+=a
    a+=1
print(sum1)

print('——————————for in 循环结构————————————————')
#in表达从（字符串，数列等）依次取值，又称遍历，for 自定义变量；
for item in "hallloword":
    pass
print(item)
for item in range(10):
    pass
print(item)
for _ in range(5):
    print('争取移民')

#用for in 循环结算1到100的累加值； 条件表达式
#用for in 循环结算1到100的偶数累加值；
sum=0
for s in range(0,101):
    sum1+=s
print(sum1)
