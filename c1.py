import datetime
from cache_utils import cache


@cache
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


t1 = datetime.datetime.now()
print(fib(300))
t2 = datetime.datetime.now()
print(t2 - t1)
