# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/28 21:55

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
Student.method()

#创建Student类的对象
stu=Student('川普',80)
print(stu.name)
print(stu.age)
stu.eat()
stu.method()

#第二种调用
Student.eat(stu)  #30行与26调用相同
print(Student.native_place)


