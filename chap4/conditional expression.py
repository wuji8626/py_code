# 一万个小时学习Python
# 累计学习1个小时
# 开发时间：2022/5/4 15:44
#conditional expression 条件表达式
#input two integers from the keybord,compare the size of the two integers
#从键盘输入两个整数，比较两个整数的大小
A=int(input('Input the first number'))
B=int(input('Input the second number'))

if A>B :
    print(A,"大于",B)
else:
    print(A,"不大于",B)

print('conditional expression is ifelse abbreviation')

print(A, "大于", B) if A>B else print(A,"不大于",B)
