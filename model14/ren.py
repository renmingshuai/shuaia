class Person:
    __age=None
    __sex=None
    __name=None
    def setage(self,age):
        self.__age=age
    def setsex(self,sex):
        self.__sex=sex
    def setname(self,name):
        self.__name=name
    def getage(self):
        return self.__age
    def getsex(self):
        return self.__sex
    def getname(self):
        return self.__name

class  Worker(Person):
    def ganhuo(self,):
        print(self.getname(),"在干活")
class Student(Person):
    def study(self):
        print(self.getname(),"在学习")
    def sing(self):
        print(self.getname(),"在唱歌")
a=Student()
a.setname("学生")
a.study()
a.sing()