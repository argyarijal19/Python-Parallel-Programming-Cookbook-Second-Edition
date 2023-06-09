from do_something import *
import time
import multiprocessing


if __name__ == "__main__":
    start_time = time.time()
    size = 1000
    procs = 10   
    jobs = []
    for i in range(0, procs):
        out_list = list()
        process = multiprocessing.Process\
                  (target=do_something,args=(size,out_list))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print ("List processing complete.")
    end_time = time.time()
    print(jobs)
    print(j)
    print("multiprocesses time=", end_time - start_time)
