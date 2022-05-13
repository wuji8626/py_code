# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/13 10:58
print('对key的判断')
it=dict(fatatily='死亡',suspect='怀疑/嫌疑犯',harness='套上驾驭/马具',disruption='扰乱',
        exclusive='独有的/独家新闻')

print('stimulus刺激' in it)

print('stimulus刺激'not in it)

print('字典元素的删除')
print('删除前',it)   #删除字典的元素
del it['fatatily']
print('删除后',it)

print('增加字典的元素')
it['stimulus']='刺激' #字典元素的新增
print(it)

it.clear()    #清空字典
print(it)

