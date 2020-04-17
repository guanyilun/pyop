from collections.abc import Iterable

@Op
def car(x):
    assert isinstance(x, Iterable)
    if len(x) == 0: return None
    return x[0]
@Op
def cdr(x):
    assert isinstance(x, Iterable)
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
