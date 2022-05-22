# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/21 22:00
#函数内的变量叫局部变量，函数外的变量叫全局变量
#用globe可以把局部变量变成全部变量

def fun(a,b):
    global c #1:把局部变量变成全局变量
    c=a+b
    return c
print(fun(20,30))
print(c)

