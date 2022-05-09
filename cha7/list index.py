# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/9 22:35
#获取列表中指定元素的的索引

lst=['halo','worldd',99,'halo']

print(lst.index('halo'))
print(lst.index('worldd'))
#print(lst.index('99')) #抛出valverror
print(lst.index(99,1,3)) #在索引1-3之间，不包含3，查找halo的索引

#获取列中的单个元素
print(lst[2])  #正向索引，从0到N-1
print(lst[-2]) #逆向索引从-N到-1
print(lst[-7]) #指定索引不存在，抛出indexerror

