#-*- coding: utf-8 -*-
__author__ = 'liveangel'
__project__ = 'PythonTutorial'

import functools
def log(text):
    if callable(text):
        #无参数
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print 'begin call: ' + text.__name__
            text(*args, **kw)
            print 'end call: ' + text.__name__
        return wrapper
    else:
        #有参数
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print 'begin call: ' + func.__name__
                func(*args, **kw)
                print 'end call: ' + func.__name__
            return wrapper
        return decorator

@log
def  now1():
    print 'doing1...'

@log('text')
def now2():
    print 'doing2...'

now1()
now2()