class O:
    """Prove that simple things do make a difference"""
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self, x):
        return self.func(x, *self.args, **self.kwargs)
    def __rmatmul__(self, other):
        return [self.func(x, *self.args, **self.kwargs) for x in other]
    def __rfloordiv__(self, other):
        return self.func(other, *self.args, **self.kwargs)

def Op_partial(i=0):
    def wrap(fun):
        """Decorator for functions that have parameters in
        all but the i-th argument."""
        class tmp:
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs
            def __call__(self, x):
                args, kwargs = self.args, self.kwargs
                args.insert(i, x)
                return fun(*args, **kwargs)
            def __rmatmul__(self, other):
                return [fun(other, *self.args, **self.kwargs) for x in other]
            def __rfloordiv__(self, other):
                return fun(other, *self.args, **self.kwargs)            
        return tmp
    return wrap


def Op(fun):
    return O(fun)

Op0 = Op_partial(i=0)
Op1 = Op_partial(i=1)
Op2 = Op_partial(i=2)
Op3 = Op_partial(i=3)

