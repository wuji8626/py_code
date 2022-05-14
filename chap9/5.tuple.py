# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/14 18:14
crown={'comfort':'安慰','campaign':'运动/竞选','conservative':'保守派',
       'propose':'建议/打算/求婚','bold':'英勇的/黑体的/厚颜无耻的','eliminate':'消除消灭','thread':'线'}
radish=dict(municipality='自治市',progressive='进步的',tropical='热带的/热情的',
            campanionship='友谊',consert='音乐会/协调协同',tangle='纠缠纠纷')
setback=dict(crawl='拍醒',skitter='轻捷的跑动',constitudion='章程/构成/宪法',
             callabrate='合作/通敌',endeavor='努力尽力',snap='折断')
tangle1=['municipality','progressive','tropical','campanionshiop','consert','radish']
setback2=['自治市','进步的','热带的/热情的','友谊','音乐会/协调协同','萝卜']
band={'observe':'观察监视','figuratively':'比喻地',90.99:90}
#元组里可以加入列表，字典，元组是不可变对象，列表和字典是可变对象
tuple1=('municipality','figuratively',90,False,tangle1,crown)
a=[1,2,3,tuple1]
setback=dict(crawl='拍醒',skitter='轻捷的跑动',constitudion='章程/构成/宪法',
             callabrate='合作/通敌',endeavor='努力尽力',snap='折断',bold=tuple1)
#元组的第二种创建方式
yuanzu=tuple(('municipality','figuratively',90,False,tangle1,crown))
#tangle1是列表 crown是字典
print('元组里面的列表和字典变更前---------')
print(yuanzu)

tangle1.append('萝卜')
del crown['campaign']
#元组是不可变对象，要变只能变列表和字典等可变对象的里面的元素

print('元组里面的列表和字典变更后---------')
print(yuanzu)
#打印后的元组，里面的列表末尾中增加了一个萝卜，里面的字典少了一个key键值，campaign

#元组的判断
print(crown in yuanzu) #用in 或者not in判断元素是否在元组当中

