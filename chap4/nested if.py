# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/4 14:30
#nested if  nest 巢穴 嵌套
#set different discouts for members and non-members

member_id=input('输入会员号')
if member_id=="Y":
    money=int(input('衣服价格'))
    if money>=200:
        print('该商品打八折')
    elif money>=100 and money<200:
        print('该商品打九折')
    else:print('该商品不打折')

else:
    money = int(input('衣服价格'))
    if money>=200:
        print('该商品打九五折')
    else:
        print('该商品不打折')
