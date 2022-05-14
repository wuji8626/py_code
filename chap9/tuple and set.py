# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/13 16:32

'''元组的两种创建方式以及空元组的创建'''
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
print('元组里面加入字典-------------------')
print(tuple1)
#列表里面可以加入元组
print('列表里面加入元组-------------------')
print(a)
print('字典里面加入元组------------------')
print(setback)

