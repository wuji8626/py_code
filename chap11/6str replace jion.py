# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/17 14:58
#字符串的替换和合并
#1：字符串替换，replace():第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法
#替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定最大替换次数；
a='murky intestine lapse lapse lapse lapse'
print(a.replace('lapse','condone'))
print(a.replace('lapse','condone',2))



#2：字符串的合并，join(),将列表或者元组中的字符串合并成一个字符串；
b=['murky','intestine','lapse']
print('|'.join(b))
print("".join(b))


