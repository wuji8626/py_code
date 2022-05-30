# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/30 13:56

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
#类属性的使用方式
print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.A='涌泉乡'
Student.native_place='九江'
print(stu1.native_place)
print(stu2.native_place)
print(Student.native_place)
print(Student.A)

#类方法的使用方式
Student.cm()
stu1.method()
stu1.eat()