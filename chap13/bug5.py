# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/23 22:45
#try……except……else……finally结构
#finally块无论是否发生异常都会被执行，能常用来释放try块中申请的资源

try:
     a=int(input('请输入第一个整数'))
     b=int(input('请输入第二个整数'))
     result=a/b
except BaseException as e:
    print('程序出错了')
else:
     print('结果为',result)
finally:
    print('无论是否发生一场都会执行的代码')

