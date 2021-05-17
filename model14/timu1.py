class Chef:
    __name=None
    __age=None
    def setname(self,name):
        self.__name=name
    def getname(self):
        return  self.__name
    def setage(self,age):
        self.__age=age
    def getage(self):
        return  self.__age
    def zhengfan(self):
        print("我在蒸饭爷爷类")
#儿子
class Chefson(Chef):
    def chaocai(self):
        super().zhengfan()
        print("我在炒菜父亲类")

#孙子
class Chefgrandson(Chefson):
    #方法的重写父类
    def chaocai(self):
        print(self.getname(),"在炒菜1")
        super().zhengfan()
        # 方法的重写  爷类
    def zhengfan(self):
        print(self.getname(),"在蒸饭1")

chef=Chefgrandson()#创建孙子对象
chef.setname("我是孙子")
chef.setage(19)
chef.zhengfan()
chef.chaocai()

