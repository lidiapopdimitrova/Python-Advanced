from math import log, e
number = int(input())
base = input()
if base == "natural":
    print(f"{log(number, e)} -natural logarithm")
else:
    print(log(number, int(base)))
# log(10)10 = 1 => 10 ^ 1 = 10

