class Address():
    __counrry = None
    __province = None
    __street = None
    __door = None
    def setCounrry(self,counrry):
        self.__counrry = counrry
    def getCounrry(self):
        return  self.__counrry
    def setProvince(self,provice):
        self.__province = provice
    def getProvicne(self):
        return self.__province
    def setStreet(self,street):
        self.__street = street
    def getStreet(self):
        return self.__street
    def setDoor(self,door):
        self.__door = door
    def getDoor(self):
        return self.__door