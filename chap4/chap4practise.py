# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/5 9:02

print('——————————————————sequential structure 顺序结构联系 practise——————————————————')
num_1=int(input('输入第一个数字')) #赋值运算符
num_2=int(input('输入第二个数字'))
print(num_1)
print(num_2 )

print('———————————————————single branch 单分支结构 practise——————————————')

if num_1<=num_2: #比较运算符 布尔运算符
    print(num_1<num_2)
if not num_1>=num_2:
    print(num_1<num_2)

print('———————————————————dual branch 双分支结构 practise——————————————')
#银行取款账号显示 withdraw money from bank

s=int(input('Please enter the withdrawal amount'))
money=10000
if s>money:
    print('对不起，超过存款金额')
else:
    print("Your overage is",money-s)

#odd number even 奇数偶数判断

A=int(input("输入数值"))
if A%2==0:     #==是比较运算符，对对象的值进行比较；
    print(A,'是偶数')
else:
    print(A,'是奇数')






