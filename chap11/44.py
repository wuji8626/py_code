# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/18 13:24

#字符串的劈分操作
str_1='hail冰雹，inspcet检查视察，implode内爆，speculate推测，rational合理的'
str_2='creepy爬行的|condo公寓|tatter破烂|shawl毛巾|clutch离合器|circuit巡回电路'

print(str_1.split(sep="，"))#劈分字符串要在在原字符串内
print(str_2.split(sep='|')) #劈分出来的为列表

print(str_2.split(sep='|',maxsplit=2))
print(str_1.rsplit(sep='，',maxsplit=2))


