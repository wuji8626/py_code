# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/17 12:21
#字符串的查找，字符串是一个顺序序列，输入子字符串，查出索引位置；
a='murky，intestine,lapse'
print(a.find('in'))#1查找子串第一次出现的位置
print(a.rfind('in'))#2查找字符串最后一次出现的位置
b='HAIRPIECE，Intestine,lapse'
#字符串的大小写转换操作，字符串是不可变序列，转换之后会产生新的字符串序列
a.upper()#1:将字符串所有小写字母转成大写,不改变原有的值
print(a)
print(a.upper())
print(b)
print(b.lower())#2:将字符串所有大写字符转成小写,不改变原有的值

c=b.swapcase()#3:将所有大写字符改为小写，所有小写字符改为大写
print(c)

print(a.capitalize())#4:将第一个字符大写，其他字母小写

print(a.title())#5:把每个单词的第一个字符大写，其他字符小写

A='murky，intestine,lapse'
B=A.lower()
print(A,id(A)) #值没有变，但是转换操作之后，ID变了
print(B,id(B))

print(A is B) #比较运算符，比较A和B的ID是否一致






