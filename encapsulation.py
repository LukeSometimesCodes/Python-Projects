

class testencapsulation:
    def __init__(self):
        self._protectedVar = 0

obj = testencapsulation()
obj._protectedVar = 25
print(obj._protectedVar)



class privatetest:
    def __init__(self):
        self.__privateVar = 25

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

    

obj = privatetest()

obj.getPrivate()

obj.setPrivate(25)

obj.getPrivate()


