#!/bin/python3
# Reference: https://stackoverflow.com/a/57794356

import time

def benchmark(fn):
    def _timing(*a, **kw):
        st = time.perf_counter()
        r = fn(*a, **kw)
        print(f"   {fn.__name__} execution: {time.perf_counter() - st} seconds")
        msg = "{:>35} took {:>6.5f} sec".format(fn.__name__, time.perf_counter() - st)
        print(msg)        
        return r

    return _timing

@benchmark
def your_test():
    print("IN")
    time.sleep(1)
    print("OUT")

your_test()