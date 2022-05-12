# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 13:42
print('''
1:移除单个元素
2:删除一个指定索引位置上的元素，不指定索引删除最后一个；
3:移除多个元素
4：清空列表
5：删除列表

''')
lst2=['major[主要的，主修科目]','chaos[混乱]',
      'gravity[重力，严重性]','destruction[破坏摧毁]','instigate[唆使]']
lst2.remove("chaos[混乱]") #移除单个元素
#lst2.lst2.remove()  romove里面的值不能为空
print(lst2)

lst2.pop(0)  #删除一个指定索引位置上的元素,括弧内输入索引,如果不执行参数将删除列表最后一个元素；
print(lst2)





lst2.clear()  #清空列表
print(lst2)

#del lst2
#print(lst2) #删除列表
print('删除列表中的多个元素')
lst2=['major[主要的，主修科目]','chaos[混乱]',
      'gravity[重力，严重性]','destruction[破坏摧毁]','instigate[唆使]']
lst2[:3]=[]
print(lst2)     #删除列表的多个元素


lst2.pop(0)
print(lst2)





