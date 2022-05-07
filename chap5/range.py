# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/5 11:14
#range的三种方式 Three ways to create a range 用来写整数序列
r=range(10) #小括号中只给一个数 ，默认从0开始，相差1,1为步长；
print(r)
print(list(r)) #用于查看range对象中的整数序列；

#第二种创建方式,给了两个参数

s=range(1,10) #从1开始到10（不包含10）结束，步长为1,相邻两数相差为1;
print(list(s))

#第三种创建方式，给了三个参数

t=range(1,10,2)
print(list(t)) #从1开始，10结束（不包含10），步长为2，序列数值为：1,3,5,7,9

#用in 和not in判断 是否在序列中

print(10 in t) #布尔值

print(10 not in t)

#range 函数是for循环的对象；



