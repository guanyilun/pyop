from fn import _

class O:
    """Prove that simple things do make a difference"""
    def __init__(self, func):
        self.func = func
    def __call__(self):
        self.func()
    def __rmatmul__(self, other):
        return [self.func(x) for x in other]
    def __rfloordiv__(self, other):
        return self.func(other)
