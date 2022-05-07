# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/5 9:59

#mutiple branches practise and  escape character 多分支结构
#escape character \n 换行 \b退格 \t四位水平制表符  \r回车 对前面的内容进行覆盖

a=int(input('输入\'成绩')) #对‘ “” \进行转义
if a>=90 and a<=100:
    print(a,'is exce\bllent!')
elif a>=80 and a<90:
    print(a,'is above \taverage!')
elif a>=70 and a<80:
    print(a, 'ave\rrage')
elif a >= 60 and a < 70:
    print(a, 'is usually the  \nminimum passing grade!')
else:
    print(a,'is failed')
print('---------nested if------嵌入式结构')

member=input('请问您是否是会员Y/N')
money=int(input("输入金融"))
if member=='Y':
    if money>=200:
      print("该件商品打8折")
    elif money>=100 and money<=200:
      print("该件商品打9折")
    else:
      print("该件商品不打折")
else:
    if money >= 200:
      print("该件商品打8折")
    elif money >= 100 and money <= 100:
      print("该件商品打9折")
    else:
     print("该件商品不打折")
