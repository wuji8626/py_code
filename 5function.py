# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/30 9:53

#1:函数的创建和调用

def func(a,b):
    c=a+b
    return c
print(func(10,20))

print(func(b=50,a=20))

print(func(50,b=70))

def func(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
print(func([20,23,34,12,7,6,9]))

def fun(*a):
    print(a)
fun([10,20,30,30,40,50])

def fun(**a):
    print(a)

fun(a=5,b=10,c=20,d=30)



