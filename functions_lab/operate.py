def operate(operator, *args):
    def add(*args):
        pass

    def subtract(x, *args):
        return x - sum(-y for y in args[1:])