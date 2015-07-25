# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'
from User import User

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()