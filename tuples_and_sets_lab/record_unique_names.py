num = int(input())

names = set()

for _ in range(num):
    names.add(input())

[print(name) for name in names]


# other way:
# num = int(input())
# names = {input() for _ in range(num)}
# [print(name) for name in names]

