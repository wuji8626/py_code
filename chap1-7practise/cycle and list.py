# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 19:34

#元组，是一个不可变序列
#1创建元组
fatality=('figuratively','offensvie','facetious','crook','womanizer',False,11)

fatality_1=('比喻地/象征性地','冒犯的/进攻','诙谐的/爱开玩笑的','弯曲/骗子','玩弄女性者')

radish=('gut','内脏/取出内脏','flexible','灵活的/柔韧的','facility','设备/天赋','lunacy','精神失常')
radish_1=tuple(('reflect','反应/反射/反省','host',
               '主人/主持','grand','宏伟的/豪华的','grant','授予/补助金'))

slam=tuple(('clemency','仁慈/温和','unveil','揭露','demonnizie','妖魔化','choke','窒息'))

print(fatality)
print(fatality_1)
print(radish)
print(radish_1)
print(slam)
#2获取元组的一个和多个元素
print(fatality[0:3])
print(fatality[-1])
#3元组的遍历
for i in radish:
    print(i)

A=[11,22,fatality]
print(A)

#位运算符

print(0b00101101 | 0b00111000)

radi={'gut':'内脏/取出内脏','flexible':'灵活的/柔韧的','facility':'设备/天赋','lunacy':'精神失常'}
radi_1=dict(reflect='反应/反射/反省',host=
               '主人/主持',grand='宏伟的/豪华的',grant='授予/补助金')
fatality=('figuratively','offensvie','facetious','crook','womanizer',False,11)

fatality_1=('比喻地/象征性地','冒犯的/进攻','诙谐的/爱开玩笑的','弯曲/骗子','玩弄女性者')
radi['gut']='取出内脏' #字典的新增和重新赋值
print(radi['gut'])
del radi_1['reflect'] #删除字典种的元素
print(radi_1)
radi_1.clear() #清除字典
print(radi_1)
print(radi.get('grand','雄伟的/豪华的')) #字典元素的获取

print(radi.keys())
print(radi.values()) #取出字典的key，value和key value
print(radi.items())
