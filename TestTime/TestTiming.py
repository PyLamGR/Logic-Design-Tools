
from datetime import date
import functools
import time


def timeit(func):

    @functools.wraps(func)
    def newfunc(*args, **kwargs):

        """save begin time"""
        start=time.time()
        print(start)

        """create a new file to save the time"""
        filename = 'Log File -- {}-3.txt'.format(date.today())
        f = open(filename, 'a')
        print(filename)

        func(*args, **kwargs)

        """save the last time"""
        end = time.time()

        """write in file the function and the time in sec"""
        f.write('function [{}] finished in {} s'.format(func.__name__, float(end-start))+"\n")

    return newfunc


"""@timeit
def foobar():
    i=1000000
    while (i>1):
        print(i)
        i=i-1
"""

if __name__ == '__main__':
    pass

