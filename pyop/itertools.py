from toolz import itertools

from .base import Op, Op0, Op1

def isiterable(x):
    try: len(x)
    except: return False
    return True
@Op
def car(x):
    assert isiterable(x)
    if len(x) == 0: return None
    return x[0]
@Op
def cdr(x):
    assert isiterable(x)    
    if len(x) == 0: return ()
    return x[1:]
@Op
def cadr(x):
    return x // cdr // car
@Op
def caar(x):
    return x // car // car
@Op
def cddr(x):
    return x // cdr // cdr
@Op
def cdar(x):
    return x // car // cdr
@Op
def caaar(x):
    return x // car // caar
@Op
def caadr(x):
    return x // cdr // caar
@Op
def cadar(x):
    return x // car // cadr
@Op
def caddr(x):
    return x // cdr // cadr
@Op
def cdaar(x):
    return x // car // cdar
@Op
def last(x):
    return x[-1]
@Op
def first(x):
    return x // car
@Op0
def filter_(x, func):
    return filter(func, x) 
@Op
def list_(x):
    return list(x)
@Op
def enumerate_(x):
    return enumerate(x)
@Op
def len_(x):
    return len(x)
@Op0
def reduce_(x, func):
    return reduce(func, x)
@Op0
def partition_(x, n):
    return itertools.partition(n, x) 
@Op0
def take_(x, n):
    return itertools.take(n, x)
@Op0
def remove_(x, func):
    return itertools.remove(func, x)
@Op0
def topk_(x, k):
    return itertools.topk(k, x)
@Op
def unique_(x):
    return itertools.unique(x)
@Op0
def plunk_(x, i):
    return itertools.plunk(i, x)
