# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/11 11:24
print('----在列表末尾添加一个元素--------')
lst=['defendant','被告，防守的','indict','控告，起诉',
     'domestic','','国内的，家人的','brutality',
     '无情残忍','division','除法，部门','overrate','高估']
print(lst,id(lst))
#Add an element to the end of the list
lst.append(99)
print(lst,id(lst))
print('----------在列表末尾添加一个元素--------------------------')
print()
print()
print('----在列表末尾至少添加1个元素---------')
#Add at least one element to the end of the list
lst1=['surface','表面']
lst.extend(lst1)
print(lst,id(lst))
print('-------------在列表末尾至少添加1个元素-----------------------')
#Add at least one element anywhere in the list

print()
print()
print('-----在元素的任意位置插入至少一个元素------------------')
lst3=[22,33,44]
lst[1:4]=lst3
print(lst)

print('-----在元素的任意位置插入至少一个元素-----------------------')

print()
print()
#Add one element anywhere in the list
print('-----在元素的任意位置插入一个元素-----')

lst.insert(1,90)
print(lst)

print('--在任意位置插入一个元素，则该位置元素被替换，原元素值后移一个位置--')