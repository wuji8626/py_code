# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/20 13:09
#函数的参数传递
def fun(arg1,arg2):
    print('arg1=',arg1)
    print('arg2=',arg2)
    arg1=100
    arg2.append(10)
    print('arg1=',arg1)
    print('arg2=',arg2)

n1=11
n2=[22,33,44]
print(n1)
print(n2)
print('----------------------')
fun(n1,n2)
print(n1)
print(n2)

