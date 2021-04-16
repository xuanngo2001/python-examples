#!/bin/python3
# Description: Sample of a running process.
# Usage:
#   python -m cProfile -s time          myscript.py <args>
#   python -m cProfile -o output.file   myscript.py <args>
#       -s : sort by => https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats

# Test: I prefer to sort by cumulative time.
#   python3 -m cProfile -s cumtime profile_py.py 

# Reference:
#   - https://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script
#   - https://docs.python.org/3/library/profile.html

import time
import random

class Runtime(object):
    def __sleep(self, sec):
        time.sleep(sec)
        
    def slow(self):
        print("slow()")
        self.__sleep(3)
    
    def fast(self):
        print("fast()")
        self.__sleep(0.275)
    
    def random(self):
        print("random()")
        r = random.randint(67,123)/100 # Between 0.67 and 1.23 seconds.
        self.__sleep(r)

def main():
    run = Runtime()
    run.slow()
    run.fast()
    run.random()
    
if __name__ == '__main__':
    main()

# >python3 -m cProfile -s cumtime profile_py.py
# slow()
# fast()
# random()
#          1368 function calls (1325 primitive calls) in 4.464 seconds
# 
#    Ordered by: cumulative time
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       4/1    0.000    0.000    4.464    4.464 {built-in method builtins.exec}
#         1    0.000    0.000    4.464    4.464 profile_py.py:15(<module>)
#         1    0.000    0.000    4.458    4.458 profile_py.py:35(main)
#         3    0.000    0.000    4.458    1.486 profile_py.py:19(__sleep)
#         3    4.458    1.486    4.458    1.486 {built-in method time.sleep}
#         1    0.000    0.000    3.001    3.001 profile_py.py:22(slow)
#         1    0.000    0.000    1.181    1.181 profile_py.py:30(random)
#         1    0.000    0.000    0.276    0.276 profile_py.py:26(fast)
#       9/1    0.000    0.000    0.005    0.005 <frozen importlib._bootstrap>:978(_find_and_load)