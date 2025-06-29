print(__name__)


class A:
    def getmodule(self):
        print(self.__module__)
print(A())


#print(__name__, A().getmodule())


