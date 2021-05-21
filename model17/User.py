class User():
    __account = None
    __username = None
    __password = None
    __address = None
    __bank = None

    def setAccount(self,account):
        self.__account = account
    def getAccount(self):
        return self.__account
    def setUsername(self,username):
        self.__username = username
    def getUsername(self):
        return self.__username
    def setPassword(self,password):
        self.__password = password
    def getPassword(self):
        return self.__password
    def setAddress(self,address):
        self.__address = address
    def getAddress(self):
        return self.__address
    def setBank(self,bank):
        self.__bank = bank
    def getBank(self):
        return self.__bank