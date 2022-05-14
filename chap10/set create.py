# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 19:27
#集合的两种创建方式
crawl={'skitter','constitution',90,
       'figutively','callaborate','setback','endeavor','snap'}

print(crawl)
#第二种使用内置函数set（）
s=set(range(6)) #输入数列 一是列表集合
print(s)
print(set([3,34,5,56])) #二是数列集合
print(set((2,34,4,45))) #三是元组集合
print(set('crawl')) #四是字符串集合
print(set({123,4,45,5}))#集合的集合
print(set()) #空集合

print(set({'skitter','constitution',90,
       'figutively','callaborate','setback','endeavor','snap'}))

#集合和字典的数据机构相同，不允许重复，会把重复的删除