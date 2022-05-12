# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 9:56
lst=['seize[抓住]','tuitoin[讲授，学费]','cocky[自大的]','phase[阶段，分阶段]','drop[降低]']

lst1=list(['dither[犹豫不决]','riot[暴乱]','bewilder[使人困惑]','terrify[恐吓]','loot[打劫]'])

lst2=list(['major[主要的，主修科目]','chaos[混乱]',
      'gravity[重力，严重性]','destruction[破坏摧毁]','instigate[唆使]'])
print(lst.index('phase[阶段，分阶段]'))
#print(lst.index('bewilder[使人困惑]'))
print(lst1[2],lst1[-3])
print( lst2[2] in lst ,type(lst2[2]))

print('''
1:获取元素的索引，用列表名.index("元素")
2:获取元素单个元素，列表名[输入元素的索引]
3：元素 （not）in 列表名 ：判断元素是否在列表当中
''')

print('列表元素的遍历')

for it in lst2:
      print(it)

for it in lst2:
      print(it,end=' ')