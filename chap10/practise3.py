# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/15 21:38
#集合间的关系判断
perpetuate={'cocky','dither','gravity','loot'}
anxiety=set({'division','sieze','drop','emulate'})
anarchy={'division','sieze','drop'}
#两个集合是否相等
print(perpetuate == anxiety)
print(perpetuate != anarchy)

#A是B的子集
print(anarchy.issubset(anxiety)) #anarchy是否是anxiety的子集 True

#A是B超集
print(anxiety.issuperset(anarchy))#anxiety是anarchy的超集 True

#A和B没有交集
print(perpetuate.isdisjoint(anxiety))#perpetuate和anxiety没有交集 True
