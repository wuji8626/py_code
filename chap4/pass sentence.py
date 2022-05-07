# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/4 16:17
'''pass sentence/statement use 什么都不做
只是一个占位符do nothing
just a placeholder'''

id=input('你是否是会员Y/N')

if id=='Y':
    pass
else:
   pass

member_id=input('输入会员号') #if 和else should be aligned
money = int(input('衣服价格'))
if member_id=="Y":
     if money>=200:
        print('该商品打八折')
     elif money>=100 and money<200:
        print('该商品打九折')
     else:
        print('该商品不打折')

else:
 if money>=200:
     print('该商品打九五折')
 else:
            print('该商品不打折')
