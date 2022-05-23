# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/23 22:37
#异常处理
try:
     a=int(input('请输入第一个整数'))
     b=int(input('请输入第二个整数'))
     result=a/b
     print('结果为',result)

#手抖或者一些例外情况导致程序崩溃
except ValueError:
    print('只能输入数字串')

except ZeroDivisionError:
    print('对不起，除数不能为0')
print('程序结束')

