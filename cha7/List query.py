# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/10 22:41

lst=["rehabilitation",'pitfall','predecesser','miscaculate','emulate','stuck',77,True]
print(lst)
print(bool('aa'not in lst)) #字符串aa不在lst列表中
print(bool('pitfall' in lst))#字符串在列表中

it=input('输入内容')
if it in lst:
    print(it,'in',lst)
#列表元素的遍历

for iterm in lst:
    print()
