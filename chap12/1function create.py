# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/20 11:13
#函数的创建

def calc(a,b): #1创建函数
    c=a+b
    return c
result=calc(10,20) #2调用函数
print(result)

def calc(c,d): #1创建函数
    e=c+d
    return e
result=calc(d=20,c=20) #2调用函数
print(result)


def calc(a,b): #1创建函数
    c=a+b
    return c
calc(10,20) #2调用函数
print(calc(10,20))