# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/9 19:39

'''a=4
print(type(str(a)))
b=int(input('输入数字'))
a=0
while a<3:
   if b>a:
      print("b大于a")
   a+=1
for c in range(1,3):
    print(c)


for it in range(1,51):
    if it%5!=0:
        continue
    print(it,end=" ")
print()'''

a=0
while a<=50:
    if a%5!=0:
        continue #此函数一直在循环，没有执行完成
    print(a,bool(a%5!=0))
    a+=1

for it in range(1,51):
    if it%5!=0:
        continue
    print(it)
