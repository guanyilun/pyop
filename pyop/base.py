class O:
    """Prove that simple things do make a difference"""
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    def __rmatmul__(self, other):
        return [self.func(x) for x in other]
    def __rfloordiv__(self, other):
        return self.func(other)

# decorator to wrap into O
def Op(fun):
    return O(fun)
