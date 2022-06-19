numbers = [int(x) for x in input().split(" ")]

target = int(input())
targets = set()
pairs = {}

for value in numbers:
    if value in targets:
        p1 = value
        p2 = pairs[value]
        print(f"{p1} + {p2} = {target}")
    else:
        targets.add(target - value)
        pairs[target - value] = value
