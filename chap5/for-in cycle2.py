# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/5 15:18

#用for in 循环结算1到100的累加值；
sum1=0
for s in range(1,101): #第一遍 sum=1,s=1,第二遍s=2,sum=3,第三遍s=3,sum=6
    sum1+=s
print(sum1)

#用for in 循环结算1到100的偶数累加值；

sum1=0
for s in range(1,101):
    if s%2==0:#第一遍 sum=1,s=1,第二遍s=2,sum=3,第三遍s=3,sum=6
      sum1+=s
print(sum1)

print('''输出100-999之间的水仙花数''')
'''举例：
153=3*3*3+5*5*5+1*1*1'''
for s in range(100,1000):#S= 整数100
    w = 0
    for r in str(s):                    #从字符串100中依次取值
        w += int(r) ** 3                # t = int(r)  # 把取出的值改为整数类型并赋值给变量                                                  # A=int(str(s))
    if int(str(s)) == w:                #对象的值不一定需要赋予变量
        print(w)
    #遍历执行完，此时w等三个数字的三次幂，
    #print(w) 此时拼出来的值为153
    #print(int(str(s)))=100
    #print(A,type(A),w,type(w))
    #当遍历一遍的时候w的取值已经改变，要对W重新赋值；









