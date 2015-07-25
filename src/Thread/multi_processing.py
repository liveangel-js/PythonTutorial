# -*- coding: utf-8 -*-
#UNIX/LINUX多进程实例
__author__ = 'liveangel'
__project__ = 'PythonTutorial'

import os


print 'Process %s start' % os.getpid()
print 'My parent id is %s' % os.getppid()
pid = os.fork()
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)