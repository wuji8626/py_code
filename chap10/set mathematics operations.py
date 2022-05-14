# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 22:27
#集合的数学操作
#1：交集操作
crown={'comfort','campaign','conservative',
       'propose','bold','eliminate','thread'}
crown_small={'comfort','campaign','conservative'} #两个结合是否相等，元素相同就相等
radish=set({'municipality','progressive','tropical',
            'campanionship','consert','tangle'})
print('crown和crown_small的交集',crown & crown_small)
print('crown和crown_small的交集',crown.intersection(crown_small))

#2：并集操作

print('crown和radish的并集',crown.union(radish))
print('crown和radish的并集',crown | radish)

#3：差集操作
radish=set({'municipality','progressive','tropical',
            'campanionship','consert','tangle'})
crown={'comfort','campaign','conservative',
       'propose','bold','eliminate','thread','progressive','consert'}

print(radish.difference(crown)) #radish减去双方相同的部分
print(crown.difference(radish))

