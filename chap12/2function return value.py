# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/20 14:28
#函数的返回值
def fun(num):
    odd=[] #存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
print(fun([10,29,34,23,44,53,55]))
#1函数没有返回值时
def fun1():
    print('mingle交融混合')

fun1() #1:如果函数没有返回值，函数调用完毕后，不需要给调用处提供数据，return可以不写

#2函数的返回值如果是一个，直接返回类型

def fun2():
    return 'hello'

res=fun2()
print(res)

#3函数的返回值在1个以上时，函数的返回值为元组

def fun3():
    return 'embarrassed尴尬的','juggle杂耍欺骗'
print(fun3())

#函数在返回时，是否需要返回值，视情况而定
