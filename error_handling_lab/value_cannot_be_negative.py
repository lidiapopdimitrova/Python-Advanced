class ValueCannotBeNegative(Exception):
    """Number is below zero"""
    pass


values = [int(input()) for _ in range(5)]

for value in values:
    if value < 0:
        raise ValueCannotBeNegative
    