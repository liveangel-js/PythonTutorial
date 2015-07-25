# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid values %s" % s)
    return 10 / n

foo('0')