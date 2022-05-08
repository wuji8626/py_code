# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/8 19:27
#二重循环中的break 和continue 用于控制本层循环

for a in range(1,4):
    for b in range(1,10):
        if b%2==0:
            continue
        print(b,end=" ")
    print()

a=100
b=int(input('请输入金额'))
if b<100:
    print(b,"小于100")
print(b,"小于100")

num=int(input("请输入一个整数"))
if num%2==0:
    print(num,'是偶数')
print(num,'是奇数')
# else是双分支机构，二选一，执行，不加else则是顺序结构；