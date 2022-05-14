# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 19:53
crawl={'skitter','constitution',90,
       'figutively','callaborate','setback','endeavor','snap'}
#集合元素的判断

print('skitter' in crawl)
print('skitter' not in crawl)

#集合元素的新增操作，用set.add(’输入key值‘)，一次添加一个元素
print('在新增操作之前',crawl)
crawl.add('municipality')
print('在新增操作之后',crawl)

#集合元素的新增操作，用set.update(’输入key值‘)，添加至少一个元素
it=[2,3] #可以是列表也可以是元组
crawl.update(it)#建立列表添加至少一个以上元素，如果输入字符串，走每一个字符串就是一个元素
print(crawl)
print()
print("集合元素的删除操作----------------") #删除一个指定元素，元素不存在抛出异常
print()
print('remove()在删除之前',crawl,id(crawl))
crawl.remove('municipality')
print('在remove()删除之后',crawl,id(crawl))

crawl.discard('municipality自治市') #如果元素不存在，不会出现异常
print('在dicard()删除之后',crawl)
crawl.discard('figutively')
print('discard元素正确',crawl)
print()
print('在没有利用pop()删除任意元素之前',crawl)
crawl.pop()      #pop()不指定元素，任意删除
print('在有效利用pop()删除任意元素之后',crawl)

crawl.clear()
print('清空集合元素',crawl)

