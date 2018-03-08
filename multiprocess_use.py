#################### 创建函数并将其作为多个进程 #################
# print("创建函数并将其作为单个进程:")
# import multiprocessing
# import time
#
# def worker_1(interval):
#     print ("worker_1")
#     time.sleep(interval)
#     print ("end worker_1")
#
# def worker_2(interval):
#     print ("worker_2")
#     time.sleep(interval)
#     print ("end worker_2")
#
# def worker_3(interval):
#     print ("worker_3")
#     time.sleep(interval)
#     print ("end worker_3")
#
# if __name__ == "__main__":
#     p1 = multiprocessing.Process(target = worker_1, args = (0,))
#     p2 = multiprocessing.Process(target = worker_2, args = (1,))
#     p3 = multiprocessing.Process(target = worker_3, args = (2,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print("The number of CPU is:" + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print("child   p.name:" + p.name + "\tp.id" +"\t"+str(p.pid))
#     print ("END!!!!!!!!!!!!!!!!!")


#################### 将进程定义为类 #################
# import multiprocessing
# import time
# print("将进程定义为类:")
# class ClockProcess(multiprocessing.Process):
#     def __init__(self, interval):
#         multiprocessing.Process.__init__(self)
#         self.interval = interval
#
#     def run(self):
#         n = 5
#         while n > 0:
#             print("the time is {0}".format(time.ctime()))
#             time.sleep(self.interval)
#             n -= 1
#
# if __name__ == '__main__':
#     p = ClockProcess(1)
#     p.start()                                         ##进程p调用start()时，自动调用run()


#################### 设置daemon执行完结束的方法 #################
# import multiprocessing
# import time
#
# def worker(interval):
#     print("work start:{0}".format(time.ctime()));
#     time.sleep(interval)
#     print("work end:{0}".format(time.ctime()));
#
# if __name__ == "__main__":
#     p = multiprocessing.Process(target = worker, args = (3,))
#     p.daemon = True
#     p.start()
#     p.join()
#     print "end!"

# !/usr/bin/env python
# -*- coding:utf8 -*-


#################### 使用类来继承原始的Process类进行处理，以下是模板 #################
# 1. 把要让子进程做的事情，都写在run函数内，父进程就只管提供数据和代码即可。

# 2. 父进程调用子进程的步骤是：首先，创建所有的子进程；其次，逐个调用所有的子进程，不允许有其他操作（因为会被阻塞）；最后，逐个调用join函数对父进程进行阻塞，保证子进程都运行完毕后再运行父进程。

# import os, os.path
# import time
# from multiprocessing import Process, cpu_count
#
# class myProcess(Process):
#     def __init__(self, *argus, **keywords):
#         # argus 和 keywords中可以包括函数名等特殊类，不仅仅是字符串，数字，序列等常见数据类型
#         Process.__init__(self)
#         self.argus = argus
#         self.keywords = keywords
#
#     def run(self):
#         # 时间统计功能最好在run内实现。该函数内实现子进程的操作。
#         start_time = time.time()
#         print("Proc %d start: %s" % (self.proc_seq, time.ctime(start_time)))
#         # 以下是核心代码，即你希望该进程做任务，是批量任务的模板
#         # 核心代码结束
#         end_time = time.time()
#         dur = end_time - start_time
#         print("Proc %d end: %s, Total time: %.2f" % (self.proc_seq, time.ctime(end_time), dur))
#
# if __name__ == "__main__":
#     import logging
#     import sys
#
#     logger = logging.getLogger()
#     formatter = logging.Formatter(
#         '[%(filename)s:%(lineno)d] - [%(asctime)s] : *%(levelname)s* | (%(funcName)s) %(message)s',
#         '%Y-%m-%d %H:%M:%S', )
#     stream_handler = logging.StreamHandler()
#     stream_handler.setFormatter(formatter)
#     logger.addHandler(stream_handler)
#     file_handler = logging.FileHandler(os.path.splitext(os.path.abspath(__file__))[0] + ".log", 'w')
#     file_handler.setFormatter(formatter)
#     logger.addHandler(file_handler)
#     logger.setLevel(logging.INFO)
#
#     from optparse import OptionParser
#
#     optparser = OptionParser()
#     optparser.add_option('-i', "--input", dest="input", action="store", default=None,
#                          help="please input the input file/foldername")
#     # optparser.add_option('-o', "--output", dest="output", action="store", default=None, help="please input the output folder name")
#
#     options, args = optparser.parse_args()
#     if len(args) != 0:
#         print("wrong arguments format!")
#         sys.exit(-1)
#
#     if options.input == None:
#         print("you have to give input or output folder or filenames!\nUsage: python thisfilename.py -i inputfolder/file -o outputfolder")
#         sys.exit(-1)
#
#     # 构建等于cpu核心个数的进程进行处理
#     core_num = cpu_count()
#
#     # 个人代码，准备好不同数目子进程的参数
#     argus_list = []
#     keywords_list = []
#
#     # 首先，创建子进程，但是不开始运行
#     threads = []
#     for iproc in xrange(len(argus_list)):
#         cur_proc = myProcess(iproc, argus_list[iproc], keywords_list[iproc])
#         threads.append(cur_proc)
#     # 创建好所有子进程后，再开始逐个运行
#     for iproc in threads:
#         iproc.start()
#
#     # 所有子进程都运行后，在进行父进程阻断
#     for iproc in threads:
#         iproc.join()
#
#     # 所有子进程完成后，回到父进程
#     logger.info("Done!")


#################当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。########################
# import multiprocessing
# import sys
#
# def worker_with(lock, f):
#     with lock:
#         fs = open(f, 'a+')
#         n = 10
#         while n > 1:
#             fs.write("Lockd acquired via with\n")
#             n -= 1
#         fs.close()
#
# def worker_no_with(lock, f):
#     lock.acquire()
#     try:
#         fs = open(f, 'a+')
#         n = 10
#         while n > 1:
#             fs.write("Lock acquired directly\n")
#             n -= 1
#         fs.close()
#     finally:
#         lock.release()
#
# if __name__ == "__main__":
#     lock = multiprocessing.Lock()
#     f = "file.txt"
#     w = multiprocessing.Process(target=worker_with, args=(lock, f))
#     nw = multiprocessing.Process(target=worker_no_with, args=(lock, f))
#     w.start()
#     nw.start()
#     print("end")


################# Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。######################## 用法与LOCK相似
# import multiprocessing
# import time
#
# def worker(s, i):
#     s.acquire()
#     print(multiprocessing.current_process().name +"\ti:"+str(i)+"\t" +"acquire")
#     time.sleep(i)
#     print(multiprocessing.current_process().name + "\ti:"+str(i)+"\t" +"release\n")
#     s.release()
#
# if __name__ == "__main__":
#     s = multiprocessing.Semaphore(2)
#     for i in range(5):
#         p = multiprocessing.Process(target = worker, args=(s,i))
#         print("multiprocessing.current_process().name:",multiprocessing.current_process().name)
#         p.start()


################# Event用来实现进程间同步通信。########################
# import multiprocessing
# import time
#
# def wait_for_event(e):
#     print("wait_for_event: starting")
#     e.wait()                                #无timeout设置，需要等待e.set()后才能执行。
#     print("wairt_for_event: e.is_set()->" + str(e.is_set()))
#
# def wait_for_event_timeout(e, t):
#     print("wait_for_event_timeout:starting")
#     e.wait(t)                                                       ##设置timeout=2 ，即过了2秒后无论如何执行下一步
#     print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))
#
# if __name__ == "__main__":
#     e = multiprocessing.Event()
#     w1 = multiprocessing.Process(name = "block",
#             target = wait_for_event,
#             args = (e,))
#
#     w2 = multiprocessing.Process(name = "non-block",
#             target = wait_for_event_timeout,
#             args = (e, 2))
#     w1.start()
#     w2.start()
#
#     time.sleep(10)
#
#
#     e.set()
#     print("main: event is set")

################# 使用多个进程池########################

import multiprocessing
import os, time, random

def Lee():
    print("\nRun task Lee-%s" % (os.getpid())) # os.getpid()获取当前的进程的ID)
    start = time.time()
    time.sleep(1)  # random.random()随机生成0-1之间的小数
    end = time.time()
    print('Task Lee, runs %0.2f seconds.' % (end - start))


def Marlon1():
    print("\nRun task Marlon-%s" % (os.getpid()))
    start = time.time()
    time.sleep(4)
    end = time.time()
    print('Task Marlon runs %0.2f seconds.' % (end - start))


def Allen():
    print("\nRun task Allen-%s" % (os.getpid()))
    start = time.time()
    time.sleep(3)
    end = time.time()
    print('Task Allen runs %0.2f seconds.' % (end - start))


def Frank():
    print("\nRun task Frank-%s" % (os.getpid()))
    start = time.time()
    time.sleep(2)
    end = time.time()
    print('Task Frank runs %0.2f seconds.' % (end - start))



if __name__ == '__main__':
    function_list = [Lee, Marlon1, Allen, Frank]
    print("parent process %s" % (os.getpid()))
    pool = multiprocessing.Pool(4)
    for func in function_list:
        pool.apply_async(func)      # Pool执行函数，apply执行函数,当有一个进程执行完毕后，会添加一个新的进程到pool中
    print('Waiting for all subprocesses done...')
    pool.close()
    pool.join()                      # 调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待素有子进程结束
    print('All subprocesses done.')
