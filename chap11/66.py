# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/18 17:03

str3='frustrate阻挠挫败,ignorant愚昧的无知的，unjustifiable无理的，frustrate，frustrate'

str4='frustrate阻挠挫败ignorant愚昧的无知的unjustifiable无理的'

str_='defraud欺骗，flea跳蚤，diaper尿布'

#字符串的替换和合并

#1:替换 .replacement()
print(str3.replace('frustrate','diaper尿布',2))
#第一个参数是原字符串，第二个参数是新字符串，第三个是替换的次数

print(str_.replace('defraud','flea'))

#2:jion()字符串的合并，列表和元组中的字符合并
str_1=('hail冰雹','inspcet检查视察','implode内爆','speculate推测','rational合理的')
str_2=['creepy爬行的','condo公寓','tatter破烂','shawl毛巾','clutch离合器','circuit巡回电路']

print('|'.join(str_1))
print(''.join(str_2))


