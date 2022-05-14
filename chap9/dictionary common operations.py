# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 16:36
radish=dict(municipality='自治市',progressive='进步的',tropical='热带的/热情的',
            campanionship='友谊',consert='音乐会/协调协同',tangle='纠缠纠纷')

#字典的判断
print('municipality' in radish) #判断用key值去判断，key在不在字典当中

#添加字典元素
radish['callaborate']='合作/通敌'
print(radish)

#删除元素
del radish['callaborate']
print(radish)

#清空字典
radish.clear()
print(radish)

radish=dict(municipality='自治市',progressive=[10,20,30],tropical='热带的/热情的',
            campanionship='友谊',consert='音乐会/协调协同',tangle='纠缠/纠纷')
print(radish)

#获取字典的keys,values 和keys values

keys=radish.keys() #获取所有的keys
values=radish.values()#获取所有的valuses
items=radish.items()#获取所有的键值对，形成元祖
print(keys)
print(values)
print(items)

#字典生成式
tangle=['municipality','progressive','tropical','campanionshiop','consert','radish']
setback=['自治市','进步的','热带的/热情的','友谊','音乐会/协调协同','萝卜']

item={tangles:setbacks for tangles,setbacks in zip(tangle,setback)}
print(item) #自定义value变量和自定义key变量用逗号分开

print(zip(tangle,setback))


