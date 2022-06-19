number = int(input())
chemicals_set = set()

for i in range(number):
    elements = input()
    [chemicals_set.add(x) for x in elements.split()]

print(*chemicals_set, sep="\n")