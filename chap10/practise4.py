# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/15 21:38
#集合的数学操作
#1：集合的交集操作
perpetuate={'cocky','dither','gravity','loot'}
anxiety=set({'division','sieze','drop','emulate','loot'})
anarchy={'division','sieze','drop'}

print(perpetuate.intersection(anxiety)) #perpetuate和anxiety的交集
print(perpetuate & anxiety)

#2：集合的并集操作
print(perpetuate.union(anxiety)) #perpetuate和anxiety的交集
print(perpetuate | anxiety)

#3：集合的差集操作
print(perpetuate.difference(anxiety)) #perpetuate和anxiety的交集
print(perpetuate - anxiety)

#3：集合的对称差集操作
print(perpetuate.symmetric_difference(anxiety)) #perpetuate和anxiety的交集
print(perpetuate ^ anxiety)

#结合的生成表达式
harness={i*i for i in range(1,10)}
print(harness)