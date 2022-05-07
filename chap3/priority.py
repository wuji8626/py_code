# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/3 13:34


'''a,b,c,d=40,13,'好好学习',True

print(type(a),type(b),type(c),type(d))
print(str(a)+str(b)+c+str(d))
print(str(a)+str(b))
print(4+3)'''
a=b=c=d=e=40
a+=30
b-=20
c*=2
d/=2
e%=2 #a=70,b=20,c=80,d=20,e=0
print(a,b,c,d,e)

e,f=20,30
print(e>f,e>=f,e<f,e<=f,e!=f,e==f)
print(e>f or e<f)
print(e>f and e<f)
print(e is f)
print(e is not f)

print('-----------------运算符优先级计算---------------------')
a,b=20,30
print(4*a>b-10,a<<1<b,a==b)
print(4*a>b-10 or a<<1<b and a==b)
print(4*a>b-10 and a<<1<b or a==b)
print(not 4*a>b-10 or a<<1<b and a==b)
print(not 4*a>b-10 and a<<1<b or a==b)#()>not>and>or
print('-----------------in / not in---------------------')
a='heloworld'
print('w' in a,'w' not in a)