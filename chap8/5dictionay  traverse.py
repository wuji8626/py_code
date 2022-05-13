# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/13 11:52

dic={'perpetuate':'使x持续','launch':"发射",'anxiety':'焦虑','anarchy':'混乱，无秩序',}

for it in dic:
    print(it,dic[it],dic.get(it)) #字典元素的遍历,把key的值赋给了变量

items=['urest', 'mob', 'sin', 'exploit', 'log']
prices=['不安，动荡的局面', '暴民/聚众滋事', '犯罪', '开发/剥削', '木头/伐木，记入航海日记，把X输入计算机']

a={item:price for item,price in zip(items,prices)} #字典生成式
print(a)
#把key改成大写
b={item.upper():price for item,price in zip(items,prices)}
print(b)
