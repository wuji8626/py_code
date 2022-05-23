# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/23 22:41
#不知道出现什么错误的情况下，else部分就是正确输出结果，二选一
try:
     a=int(input('请输入第一个整数'))
     b=int(input('请输入第二个整数'))
     result=a/b
except BaseException as e:
    print('程序出错了')
else:
     print('结果为',result)



