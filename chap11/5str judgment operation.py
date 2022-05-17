# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/17 14:22
#判断字符串的操作方法
a='murky intestine lapse'
a_1="   \t    "
#1：isidentifier():判断指定的字符串是不是合法的标识符
#合法的标识符是字符，数字，下划线，中文也是字符
print(a.isidentifier())

#2: isspace():判断指定的字符串是否全部由空白字符组成（回车，换行，水平制表符）
print(a_1.isspace())

#3：isapha():判断指定的字符串是否全部由字母构成
print(a.isalpha())
#4：isdemical():判断指定的字符串是否全部由十进制的数字组成
print(a.isdecimal())
#5：isnumeric():判断指定的字符串是否全部由数字组成
print(a.isnumeric())
#6：isalnum():判断指定字符串是否全部由字母和数字组成
print(a.isalnum())


