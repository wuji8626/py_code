# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/8 16:18

#打印一个四行五列矩形
for iterm in range(4):
    for iterm1 in range(5):
        print('*',end='\t')
    else:print()

#打印一个9行9列的直角三角形
for a in range(1,10): #iterm等于1时打印1个，iterm等于2时打印两个
    for b in range(1,10):
        if b<=a:
            print("*", end='\t')

    else:print()

#不换行输出的打印
print("1",end="2")
print()
print(2)
print('*', end='\t')
print()
print('*', end='\t') #可以理解为一个不换行输出的函数
print()

#打印99乘法表
for a in range(1,10):
    for b in range(1,10):
        if b<=a:
            c=a*b
            print(str(c)+'='+str(a)+"*"+str(b),end="  ")
    else:print()

for a in range(1,10):
    for b in range(1,a+1):
        print("*",end="")
    print()