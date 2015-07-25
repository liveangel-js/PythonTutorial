# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

class MyObject(object):
    def __init__(self):
        self.x = 9
        self.__y = 12
    def power(self):
        return self.x * self.x
    def energy(self):
        return self.z * self.z

obj = MyObject()
obj.q = 5
print(obj.q)
print(obj.power())
print(hasattr(obj,'x'))
print(hasattr(obj,'_MyObject__y'))
print(hasattr(obj,'__y'))

print(setattr(obj,'x',10))
print(obj.power())
print(setattr(obj,'z',10))
print(hasattr(obj,'z'))
print(obj.energy())