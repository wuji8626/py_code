# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 12:04
print('''
1:在列表的末尾添加一个元素；
2：在列表的末尾添加至少一个元素；
3：在列表的任意位置添加一个元素；
4：在列表的任意位置添加至少一个元素；
5：添加函数操作，不支持赋值,也不支持打印；
''')
lst=['seize[抓住]','tuitoin[讲授，学费]','cocky[自大的]','phase[阶段，分阶段]','drop[降低]']

lst1=list(['dither[犹豫不决]','riot[暴乱]','bewilder[使人困惑]','terrify[恐吓]','loot[打劫]'])

lst2=['major[主要的，主修科目]','chaos[混乱]',
      'gravity[重力，严重性]','destruction[破坏摧毁]','instigate[唆使]']

'''it="bewilder"
lst.append(it)
print(lst)'''

lst.append('instigate')
print(lst)

it1=['dither','tuition']
lst1.extend(it1)
print(lst1)

lst2=['major[主要的，主修科目]','chaos[混乱]',
      'gravity[重力，严重性]','destruction[破坏摧毁]','instigate[唆使]']

lst2.insert(1,"cocky")
print(lst2)

lst2[1:4]=it1 #切片是替换了原来的元素，相当于切掉
print(lst2)


lst=['seize[抓住]','tuitoin[讲授，学费]','cocky[自大的]','phase[阶段，分阶段]','drop[降低]']

lst.insert(7,'instigate')
print(lst)




