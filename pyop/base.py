class O:
    """Prove that simple things do make a difference"""
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self, x):
        return self.func(x, *self.args, **self.kwargs)
    def __rmatmul__(self, other):
        return [self(x) for x in other]
    def __rfloordiv__(self, other):
        return self(other)

def Op(fun):
    """Decorator for simple one argument function"""
    return O(fun)

def Op_partial(i=0):
    def wrap(fun):
        """Decorator for functions that have parameters in
        all but the i-th argument."""
        class tmp(O):
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs
            def __call__(self, x):
                args, kwargs = self.args, self.kwargs
                args.insert(i, x)
                return fun(*args, **kwargs)
        return tmp
    return wrap

Opp = Op_partial(i=0)
