# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/29 0:52
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')
#stu1=Student('张三',20)
stu2=Student('李四',30)
#stu1.eat()
stu2.eat()

def show():
    print('我是一个函数')


stu2.gender="男"
print(stu2.name,stu2.age,stu2.gender)
stu2.show=show
stu2.show()