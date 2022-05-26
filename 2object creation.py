# 一万个小时学习Python
# 持续付出 持续输出
# 开发时间：2022/5/26 22:42
class Student: #类名由一个或者多个单词组成，每个单词的首字母必须是大写，其余的小写

    def __init__(self,name,age):
        self.name=name #slef.name称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实例属性
        self.age=age

    #一类属性
    native_pace='吉林' #1直接写在类里的变量，称为类属性

    #二实例方法
    def eat(self): #2在类之外定义的称为函数，在类之内定义的称为方法
        print('学生在吃饭……')

   #三静态方法
    @staticmethod
    def methoe(): #3静态方法不允许写self
        print('我使用了staticmethod进行修饰，所以我是静态方法')

   #四类方法
    @classmethod
    def mc(cls):
       print('我是类方法，因为我使用了classmethod进行修饰')

stu1=Student('张三',20)