# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/4 12:50
#dual branch 双分支结构，双路结构 二选一执行

money=1000
s=int(input('输入取款金融'))
print(id(100>1),type(100>1),100>1)
if s>money:
    print('余额不足') #条件为真，执行条件体1
    money -= s
else:
    print("取款成功，余额为：",money) #条件为假，执行条件体为2

#判断奇数偶数  odd number even
A=int(input('Please enter a value'))
if A%2==0:
    print('Even')
else:
    print('Odd number')





