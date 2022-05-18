# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/18 15:53

str3='frustrate，阻挠挫败ignorant，愚昧的无知的，unjustifiable无理的'
str4='frustrate阻挠挫败ignorant愚昧的无知的unjustifiable无理的'
str_='defraud欺骗，flea跳蚤，diaper尿布'
#字符串的判断操作
#1：isidetifier(),判断字符串是不是合法的标识符,字母数字下划线
print(str3.isidentifier())#False
print(str4.isidentifier()) #True

#2:isspace(),判断字符串是否是空字符串，制表符，回车，空格
print(' \t  '.isspace()) #空字符串
print(str4.isspace())#不是空字符串

#3：isalpha(),判断字符串是否全部由字符组成

print(str3.isalpha())#flase
print(str4.isalpha())#True

#4:isdemical(),判断字符串的值是否由十进制数字组成
print('11233022'.isdecimal()) #True
print(str4.isdecimal())#False

#5:isnumeric(),判断字符串的值是否全部由数字组成
print('123四'.isnumeric()) #True

#6:isalnum(),判断字符串是否全部由数字和字母组成
print(str4.isalnum())