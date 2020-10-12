import multiprocessing
import os
import numpy as np
cpus = multiprocessing.cpu_count()


def worker(shell_cmd):
    for cmd in shell_cmd:
        print(cmd)
        os.system(cmd)
def sample():
    shell_list = ["mkdir aa", "mkdir bb", "mkdir cc"]

    p = multiprocessing.Pool()
    for vl in np.array_split(np.array(shell_list), cpus):
        p.apply_async(worker, args=(vl,))
    p.close()
    p.join()


if __name__ == '__main__':
    sample()



