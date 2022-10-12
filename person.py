class Person:
    def __init__(self, name:str):
        self.__Name = name
        self.__Presents = []

    def AddChristmasPresent(self, present):
        self.__Presents.append(present)

    def GetTotal(self):
        sum = 0
        for p in self.__Presents:
            sum = sum + p.GetPrice()
        return sum

    def GetName(self):
        return self.__Name

