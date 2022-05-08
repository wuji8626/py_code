# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/7 17:51

#flow control statement
#ATM取款超过三次退出
a=0
while a<6:
    a+=1
    if a>2:
        break
print("您的账号被锁定！")

print('-------------设置一个密码，当账号输入超过三次时，账号被锁定——————————')
a=int(input('请输入你的密码'))
b=10086
c=0
while c<10:
    if a!=b:
        print('你的密码输入错误')
    c+=1
    if c==3:
        break
print("您的密码输入错误超过三次，账号已被锁定")

print('-------------设置一个密码，当账号输入超过三次时，账号被锁定——————————')
a=int(input('请输入你的密码'))
b=10086
c=0
while c<10:
    if a!=b:
        input("请重新输入密码")
    c+=1
    if c==2:
        break
print("您的密码输入错误超过三次，账号已被锁定")