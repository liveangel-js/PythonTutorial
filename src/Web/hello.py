# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, web!</h1>'
