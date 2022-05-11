# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/11 14:50
print('//一次删除一个操作，重复的元素只删除第一个，元素不存在抛出valueerror')
lst=['defendant','被告，防守的','indict','控告，起诉',
     'domestic','domestic','国内的，家人的','brutality',
     '无情残忍','division','除法，部门','overrate','高估']
lst.remove('domestic') #一次删除一个操作，重复的元素只删除第一个，元素不存在抛出valueerror
print(lst)   #括弧内输出列表元素
#lst.remove('haha'
#print(lst)
print('//一次删除一个操作，重复的元素只删除第一个，元素不存在抛出valueerror')
print()

print("//删除一个指定索引位置上的元素，不指定时删除最后一个原色，")

lst.pop(0)  #括弧内输出索引，如果单独打印出该函数会显示什么
print(lst)

lst.pop(0)
print(lst)

print("//删除一个指定索引位置上的元素，不指定时删除最后一个原色，")
print()

print("//一次至少删除一个元素")


lst[1:4]=[]
print(lst)



print("//一次至少删除一个元素")

print("//清空列表--------------------，")
lst.clear() #清空列表
print(lst,type(lst))

print("//清空列表--------------------，")

print("//删除列表--------------------，")

del lst

print(lst,type(lst))

print("//删除列表--------------------，")
