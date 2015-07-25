# -*- coding: utf-8 -*-

__author__ = 'liveangel'
__project__ = 'PythonTutorial'

#进程间通讯 Queue

from multiprocessing import Process, Queue
import os, time, random

#写数据进程
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to Queue...' % value
        q.put(value)
        time.sleep(random.random())

#读数据进程
def read(q):
    while True:
        value = q.get(True)
        print 'Get value %s from Queue.' % value

if __name__ == '__main__':
    q = Queue()
    p = Process()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

