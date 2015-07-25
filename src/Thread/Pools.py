# -*- coding: utf-8 -*-
#线程池实例
__author__ = 'liveangel'
__project__ = 'PythonTutorial'

from multiprocessing import Pool
import os, random, time

def long_time_task(name):
    print 'Run task %s (%s)' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 5)
    end = time.time()
    print 'Task %s take time cost %f' % (name, end - start)

if __name__ == '__main__':
    print "Parent Process %s start" % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print "Wait for subprocess processing..."
    p.close()
    p.join()
    print 'All subprocesses done.'