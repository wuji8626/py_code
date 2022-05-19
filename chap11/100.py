# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/19 15:35
#编码与解码
str3='frustrate阻挠挫败,ignorant愚昧的无知的，unjustifiable无理的，frustrate，frustrate'
str4='frustrate阻挠挫败ignorant愚昧的无知的unjustifiable无理的'
str_='defraud欺骗，flea跳蚤，diaper尿布'
s="欺骗跳蚤尿布"

#1字符的编码，把字符编码成二进制
A=s.encode(encoding='GBK')#一个中文占2个字节
print(A)

A=s.encode(encoding='UTF-8')#一个中文占3个字节
print(A)

#2字符的解码，把二进制解码成字符

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))

