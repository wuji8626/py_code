# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/17 13:26
#字符串的劈分操作
#1：split（）,从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表；
#以通过参数sep指定劈分字符串的劈分符
#通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的子串会单独作为一部分
a='murky intestine lapse'
A=a.split() #空格劈分
print(A)
a1='murky|intestine|lapse|murky'
B=a1.split(sep='|')
print(B)
B1=a1.split(sep='|',maxsplit=2)#从左往右劈分两次，后面不劈分，单独做为一部分
print(B1)

#1：rsplit（）,从字符串的右侧开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表；
#以通过参数sep指定劈分字符串的劈分符
#通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的子串会单独作为一部分
a1='murky|intestine|lapse|murky'
B=a1.rsplit(sep='|')
print(B)
B1=a1.rsplit(sep='|',maxsplit=2)#从右边往左劈分两次，后面不劈分，单独做为一部分
print(B1)

