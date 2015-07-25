# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'
#跨平台多进程实例

from multiprocessing import Process
import os


def run_proc(name):
    # print 'Running child thred $s (%s)' % (name, os.getpid())
    print 'Run child process %s (%s)...' % (name, os.getpid())


if __name__ == '__main__':
    print "Parent Process start %s." % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Child Process will start'
    p.start()
    p.join()
    print 'Process end.'