# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/9 21:31

lst=[1,"加油",2.2,False]
print(lst)
lst1=[1,"加油",2.2,False]

a=list([1,"加油",2.2,False])
print(a)

print(type(lst))
print(type([1,"加油",2.2,False]),id([1,"加油",2.2,False]),id(lst)) #虽然值相同，但是ID并不相同
print(id(lst),id(lst1))

#列表的特点，1：列表元素按照顺序有序排序
#2：索引映射出唯一个数据
#3：列表可以存储重复数据
#4：任意数据类型混存
#5：根据需要动态分配和回收内存

print(lst[-1])  #不加括弧为列表索引







