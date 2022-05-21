# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/21 12:10

def fun(a,b='feces'):
    print(a,b)

#函数的调用

fun('粪便')
fun('conventional','传统的')

def fun(*a): #个数可变的位置形参，输出的是元组
    print(a)
fun(10)
fun(10,20,30)

def fun(**b):#个数可变的关键字形参
    print(b)
fun(b=10)
fun(a=10,b=20,c=30) #个数可变的关键字

