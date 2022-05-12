# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 10:52
lst=['seize[抓住]','tuitoin[讲授，学费]','cocky[自大的]','phase[阶段，分阶段]','drop[降低]']

lst1=list(['dither[犹豫不决]','riot[暴乱]','bewilder[使人困惑]','terrify[恐吓]','loot[打劫]'])

lst2=list(['major[主要的，主修科目]','chaos[混乱]',
      'gravity[重力，严重性]','destruction[破坏摧毁]','instigate[唆使]'])

print('''
一:切片，获取多个元素
二：list[start:stop:step]
  1：如果step为正数，从start开始，到stop结束，不包含
    stop,如果start为空则是列表首个元素，从sart往前数
    如果stop为空则代表最后一个元素，如果step为空则默认为1；顺序切片
  2:如果step为负数，则start开始，到stop结束，不包含stop,
    如果start为空则，则是列表的最后一个元素，stop为空默认
    是列表第一个元素；逆序切片
    
''')
print(lst2[:],lst2[0:])
print(lst2[1:4])
print(lst2[:4:2])

lst1=list(['dither[犹豫不决]','riot[暴乱]','bewilder[使人困惑]','terrify[恐吓]','loot[打劫]'])
print("-----step为负值时-----")
it=lst1[4::-1]
print('step为负值时',it)



