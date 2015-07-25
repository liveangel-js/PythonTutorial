# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

import time, threading, os

def loop():
    print "%s thread is running." % threading.currentThread().name

    for i in range(0,5):
        print "Thread %s >>> %s" % (threading.currentThread().name, i)
        time.sleep(1)

    print "%s thread end." % threading.currentThread().name

if __name__ == '__main__':
    print "Process %s start." % os.getpid()
    print 'thread %s is running...' % threading.current_thread().name
    t = threading.Thread(target=loop, name = 'LoopThread')
    t.start()
    t.join()
    print 'thread %s ended.' % threading.current_thread().name