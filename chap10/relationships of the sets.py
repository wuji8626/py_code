# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 21:25
#集合间的关系
#两个集合是否相等

crown={'comfort','campaign','conservative',
       'propose','bold','eliminate','thread'}
crown_small={'comfort','campaign','conservative'} #两个结合是否相等，元素相同就相等
radish=set({'municipality','progressive','tropical',
            'campanionship','consert','tangle'})
print(crown == crown_small)

#一个集合是否是另一个集合的子集，
print('crown_small是否是crown的子集',crown_small.issubset(crown)) #crown1是否是crown的子集

#一个集合是否是另一个结合的超集
print('crown是否是crown_small的超集',crown.issuperset(crown_small))#crown是否是crown1的超集

#两个结合是否有交集
print(crown_small.isdisjoint(radish)) #两个集合没有交集，为真，返回True








radish=set({'municipality','progressive','tropical',
            'campanionship','consert','tangle'})
print(radish)
setback=set({'crawl','skitter','constitudion',
             'callabrate','endeavor','snap'})

