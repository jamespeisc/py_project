class A:
    a = 1
    def __init__(self,a):
        self.a = a
class B(A):
    def __init__(self,b,c):
        A.__init__(self,b+c)
        self.b = b
        self.c = c
        #self.a = 7
    def printv(self):
        print(self.b,self.c)
        print(self.a) #找A类的字典里，不是a的实例

b = B(4,5)
b.printv()