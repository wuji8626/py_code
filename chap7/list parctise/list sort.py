# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 15:05


lst=['seize[抓住]','tuitoin[讲授，学费]','cocky[自大的]','phase[阶段，分阶段]','drop[降低]']
print('原列表',id(lst),lst)
lst.sort()
print('新列表',id(lst),lst)


lst1=[22,11,35,14,78,26]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)nj

print('使用内置函数sorted对列表进行排序，讲改变列表的id')

lst2=[22,11,35,14,78,26]
print('原列表',lst2,id(lst2))
#开始排序

se_lst=sorted(lst2,reverse=True)
print('新列表',se_lst,id(se_lst))


