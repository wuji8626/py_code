# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/21 22:25
#递归函数recursive funcion
#1使用递归函数来计算阶乘

def fun(n):
    if n==1:
        return 1
    else:
        return n*fun(n-1)

print(fun(6))