# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

try:
    f = open ('test.txt','w')
    f.write("aaa2")

    # print f.read()
except IOError, e:
    pass
    print "IOError"
finally:
    if f:
        f.close()


with open('/path/to/file', 'r') as f:
    print f.read()