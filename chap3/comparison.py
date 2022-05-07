# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/3 11:09
#comparison oparetor 比较运算符

a,b=10,20

print('a>b吗',a>b) #False
print('a<b吗',a<b) #True
print('a>=b吗',a>=b)#False
print('a<=b吗',a<=b)#True
print('a!=b吗',a!=b)#True

print('a==b吗',a==b)

a=10
b=10
print(a==b,id(a),id(b),id(10)) #说明a与b的value相等
print(a is b) #说明a与b的id相同

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(id(55))
print(id(lst1),id(lst2))
print(lst1==lst2) #True
print(lst1 is lst2)#False

