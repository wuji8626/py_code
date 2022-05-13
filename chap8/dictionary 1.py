# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/13 9:32
print('''
1:通过{}以及dict()创建字典
2：获取字典种的元素，dict[’键‘] dict.get('键')
3：字典和列表里的元素ID都是不同的
4:当字典种元素不存在时输出不同
''')
dic={'perpetuate':'使x持续','launch':"发射",'anxiety':'焦虑','anarchy':'混乱，无秩序',}

iterm=dict(urest='不安，动荡的局面',mob='暴民/聚众滋事',sin='犯罪',exploit='开发/剥削',
           log='木头/伐木，记入航海日记，把X输入计算机')
it=dict(fatatily='死亡',suspect='怀疑/嫌疑犯',harness='套上驾驭/马具',disruption='扰乱',
        exclusive='独有的/独家新闻')

print(dic)
print(dic['perpetuate'],id(dic['perpetuate']))
print(dic['anxiety'],id(dic['anxiety']))

'''lst=[1,2,45,'anarchy']
print(lst[0],id(lst[0]))
print(lst[3],id(lst[3]))
'''
print(iterm.get('mob'))

print(iterm.get('stimulus刺激')) #返回none
print(iterm.get('stimulus刺激','inpact影响')) #当key对应的值不存在返回inpact
print(iterm['stimulus刺激']) #返回keyerror


