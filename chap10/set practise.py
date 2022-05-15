# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/15 20:31
#集合的练习，集合是一个可变对象,无序的对象,他是集合的keys值不可重复
#集合的两种创建方式
endeavor={'cocky','dither','gravity','loot'}
overrate=set({'division','sieze','drop','emulate'})
a=({})   #空集合怎么创建
print(endeavor,id(endeavor),type(endeavor))
#print(overrate,id(overrate),type(overrate))
#print(a,type(a))

#集合的操作，添加，删除，清空
endeavor.add('predecessor') #添加一个元素
print('通过.add()添加一个元素',endeavor)
list=['division','sieze']
endeavor.update(list) #至少添加一个元素，通过列表
print('通过.update(list)添加多个元素',endeavor)
endeavor.update(overrate) #通过集合添加多个元素
print('通过.update(set)添加多个元素',endeavor)
a=dict(pitfall='陷阱',defendant='被告/防御的')    #新增字典新增多个元素
endeavor.update(a)
print('通过.update(dict)添加多个元素',endeavor)
b=('indict','domestic') #只有元组，列表，都是字符串是才有用
endeavor.update(b)  #通过元组新增key值
print('通过.update(tuple)添加多个元素',endeavor)

perpetuate={'cocky','dither','gravity','loot'}
anxiety=set({'division','sieze','drop','emulate'})
print('通过.remove(\'keys\')删除1个之前',perpetuate)
perpetuate.remove('cocky')
print('通过.remove(\'keys\')删除1个元素',perpetuate)
perpetuate.pop()
print('通过.pop()删除任意一个元素',perpetuate)
perpetuate.discard('exploit') #删除一个指定的元素，不存在时不报错
perpetuate.clear()
print('通过.clear()删除集合',perpetuate)

