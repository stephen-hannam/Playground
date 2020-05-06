from enum import Enum

class Thing(Enum):
    A = 0
    B = 1
    C = 2
    def __init__(cls, **kwargs):
        for k,v in kwargs.items():
            cls.k = v

    @classmethod
    def _missing_(cls, value):
        return super()._missing_(value)

class AnotherThing:
    A = 0
    B = 1
    C = 2
    def __init__(self, var, var_type):
        self.var = var
        self.var_type = var_type

atype = Thing.A
print(atype)
athing = AnotherThing("0", AnotherThing.B)
print(athing.var)
print(athing.var_type)

a = Thing(A='a', B='b', C='c')
print(a.A)
