# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

import os
print os.name
print os.uname()
print os.environ
print os.getenv('PATH')
print os.path.abspath('.')
print os.listdir('.')
print os.pardir
print os.curdir
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']