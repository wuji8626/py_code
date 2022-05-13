# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/12 22:04
print('------创建字典--------')
dic={'张三':20,'李四':100} #字典是一个无序的序列
print(dic)

a=dict(name='jack',age=20 ) #通过内置函数创建字典
print(a)

b={} #空字典
print(b)

print('字典中元素的获取')

print(dic['张三']) #如果字典种不存在指定的key，则返回keyerror

print(dic.get('张三'))#get方法取值，如果字典中不续债指定的key，

print(dic['张三'])

print(a['name'])

print(dic.get('王五'))

#并不抛出keyerror二师返回None,可以通过参数设置默认的value,以便指定的key
#不在时返回