# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/3 10:17
#assignment oparetor 赋值运算符 从右往左计算

a=b=c=20

print(a,id(a))
print(b,id(b))
print(c,id(c))
print(id(20))

a=-40
a%=30
print(a,id(a))

a,b,c='杭州加油',30,True

print(a+str(b)+str(c))

print(a,b)

a,b=b,a

print(a,b)


