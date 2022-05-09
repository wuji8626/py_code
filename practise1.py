# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/8 20:11
#输出1-50之间所有5的倍数
#如果密码输入正确则显示输入正确，如果密码错误则显\n示密码错误，输入错误密码超过三次!')
#输出一个三行四列的矩形
#输出一个直角三角形
#打印99乘法表
#不换行的输出打印
#else 循环
#continue 和 break流程控制语句

'''print('输出1-50之间所有5的倍数')
a=1
while a<=50:
    if a%5==0:
      print(a,end=" ")
    a+=1
print()
for it in range(1,51):
    if it%5==0:
        print(it,end=" ") #打行的逻辑没明白
print()
print("如果密码输入正确则显示输入正确，如果密码错误则显\n示密码错误，输入错误密码超过三次!")
a=0
while a<3:
    b=int(input("输入密码"))
    if b==8626:
        print("密码正确")
        break
    else:print("密码错误")
    a+=1
else:
    print("您输入的错误密码超过三次")'''

#用conitue
'''a=1
while a<=50:
    if  a%5!=0:
        continue
    print(a)
    a+=1'''

print("continue 和 while循环在一起慎重，输出的不知道是什么玩意")


for it in range(1,51):
    if it%5!=0:
        continue
    print(it,end=" ")
print()

print("输出一个三行四列的矩形")

for a in range(1,4):
    for b in range(1,5):
        print("*",end=" ")
    print()

print("输出直角三角形")
for a  in range(1,10):
    for b in range(1,10):
        if b<=a:
            print('*',end=" ")
    print()        #此处print为什么不能和if平行；

print("打印一个99乘法表")

for a  in range(1,10):
    for b in range(1,10):
        if b<=a:
            c=a*b
            print(c,'=',a,"*",b,end=" ")
    print()


