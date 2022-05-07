# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/4 12:17

a=20
if a>1 :print(1)

money=10000
s=int(input('请输入取款金额'))
if s>10000 :print('余额不足')
if s<=1000 :print('取款成功')

s=input('输入')
print(id(input('输入')),id(s),id(input('234'))) #input就是你输入的字符串内容

money=10000
s=int(input('请输入取款金额'))
if s<10000 :
    money-=s
    print('取款成功，余额为',money)

