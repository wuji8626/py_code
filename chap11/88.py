# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/18 22:36
#字符串的切片操作
str3='frustrate阻挠挫败,ignorant愚昧的无知的，unjustifiable无理的，frustrate，frustrate'
str4='frustrate阻挠挫败ignorant愚昧的无知的unjustifiable无理的'
str_='defraud欺骗，flea跳蚤，diaper尿布'
a=str3[:5] #将产生一个新的字符串
print(a)
print(str3[6::2]) #切片的正值和负值走向，正值是从左往右，负值时从右向左；

print(str3[-10:])
print(str3.rfind('fru'))
print(str3[56::-1])


