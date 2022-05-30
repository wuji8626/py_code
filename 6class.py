# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/30 15:04
class Student:
    native_place='江西'
    def __init__(self,name,age):
        self.name=name #将局部变量name赋给实例属性
        self.age=age

    native_pace='吉林'
    def eat(self):
        print('学生在吃饭……')

    @staticmethod
    def method():
        print('使用staticmethod进行修饰，所以我是静态方法')

    @classmethod
    def cm(cls):
        print('我是类方法，使用calssmethod进行修饰')

stu1=Student('张三',20)
stu2=Student('李四',30)
stu1.gender='女'
print(stu1.gender)

def show():
    print('定义在类之外的称为函数')
stu1.show=show
stu1.show()
