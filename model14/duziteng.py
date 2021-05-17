
class Cook:
    __name = ""
    __age = 0

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age
    def zhengfan(self):
        print("这是",self.getName(),"蒸的饭")

class Zilei(Cook):
    def chaocai(self):
        print("这是",self.setName,"炒菜")

class Zizilei(Zilei):
    def zhengfan(self):
        print("蒸饭")
    def chaocai(self):
        super().zhengfan()
        print("炒菜")


z = Zizilei()
z.setName("张三")
z.setAge(11)
print(z.getName(),z.getAge())
z.chaocai()