# 1 产生一个进程
import multiprocessing

def foo(i):
    print ('called function in process: %s' %i)
    return

def multiprocess():
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()

if __name__ == '__main__':
	
    multiprocess()