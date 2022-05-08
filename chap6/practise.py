# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/8 13:37

#输出1-50之间所有5的倍数

'''for s in range(1,51):
    if s%5==0:
        print(s)'''

for s in range(1,51):
    if s%5!=0:
        continue #如果条件为真继续循环，
        #函数之间的层次关系，和continue平行的后面代码无效
        print(s) #与continue和break平行的函数代码均无效
print(s)


for s in range(1,51):
    if s%5!=0:
        break #结束循环
        #函数之间的层次关系，和continue平行的后面代码无效
    print(s)
print(s)

print('如果密码输入正确则显示输入正确，如果密码错误则显\n示密码错误，输入错误密码超过三次!')

for item in range(3):
    a=int(input("输入密码"))
    if 8626==a:
        print('密码正确')
        break #break 用于结束循环机构
    else:
        print("密码错误")
else:
    print('对不起您输入的错误密码超过3次') #第三次循环时执行，还是在循环内的







