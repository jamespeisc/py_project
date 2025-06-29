class Temperature:
    def __init__(self,t,unit='c'):
        self._c = None
        self._f = None
        self._k = None

        if unit == 'f':
            self._f = t
            self._c = self.f2c(t)
        elif unit == 'k':
            self._k = t
            self._c = self.k2c(t)
        else:
            self._c = t
    @property
    def c(self):
        return self._c
    @c.setter
    def c(self,value):
        self._c = value
        #convertall(self._c, unit='c')
    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f
    @property
    def k(self):
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k


########################以下为工具的方式###############################
    @classmethod
    def c2f(cls,c):
        return 9 * c /5 +32
    @classmethod
    def f2c(cls,f):
        return (f -32) *5 /9
    @classmethod
    def c2k(cls,c):
        return c + 273.15
    @classmethod
    def k2c(cls,k):
        return k - 273.15
    @classmethod
    def f2k(cls,f):
        return cls.c2k(cls.f2c(f))
    @classmethod
    def k2f(cls,k):
        return cls.c2f(cls.k2c(k))

print(Temperature.c2k(104))

class Item:
    def __init__(self,type_id,mark, **kwargs):
        kwargs.update({'t_id':type_id})
        self._spec = kwargs
    def __repr__(self):
        return str(sorted(self.__spec.items()))
class Cart:

    def additem(self,item:Item):
        pass



