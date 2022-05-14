# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 15:56
crown={'comfort':'安慰','campaign':'运动/竞选','conservative':'保守派',
       'propose':'建议/打算/求婚','bold':'英勇的/黑体的/厚颜无耻的','eliminate':'消除消灭','thread':'线/穿过'}
print(crown)

thread=crown.get('eliminate') #通过get（）获取value
print(thread)


'''radish=[1,2,32]
bold=list([1,2,23]) #用list函数建立列表是里面小括弧里面加方括号,用字典函数建立时则不用加大括号;
print(radish,bold)'''
it=crown['propose']
print(crown['campaign'],id(crown['campaign']),type(crown['campaign']))
print(it,id(it),type(it))

band={'observe':'观察监视','figuratively':90,False:90}
bold=band['figuratively'] #方括号内输入列表的key,字典是一对键值对
print(bold,type(bold))    #字典通过key来查找输出value，key可以是字符，浮点，整数，布尔类型；
new_bold=band[False]
print(new_bold,type(new_bold))

thread=crown.get('eliminate') #通过get（）获取value
print(thread)

thread=crown.get('threat')
print(thread,'威胁')  #如果threat不存在则输出none，并可以自定义不存在时自定义输出的对象

#字典里面可以包涵列表