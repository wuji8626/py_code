# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/21 10:48
#1:位置实际参数
def fun(a,b): #a,b为形势参数，简称形参，形参的位置在函数的定义处
    c=a+b
    return c #结束这个函数 并把C返回给函数调用处
result=fun(10,20) #10,20为实际参数，简称实参，参数的位置是函数的调用处
print(result)

#2：关键字实际参数
def fun(a,b):
    c=a+b
    return c #结束这个函数 并把C返回给函数调用处
result=fun(b=30,a=50)
print(result)

#3:给列表[22,33,44]末尾添加一个元素10
def calc(arg1,arg2):
    agr1=100
    arg2.append(10)
    print(agr1)
    print(arg2)

n1=20
n2=[22,33,44]
print(n1)
print(n2)
print('-------------------------')
calc(n1,n2)
print(n1)
print(n2)

#1；在函数调用过程中，进行参数的传递，如果是不可变对象，在函数体的修改
#不会影响实参的值
#2：如果是可变对象，将会营销实际参数的值；
#值是否影响取决于是否是可变对象
