length = [int(x) for x in input().split()]
length_1 = length[0]
length_2 = length[1]
numbers_set1 = set()
numbers_set2 = set()

for i in range(length_1):
    numbers_set1.add(input())

for u in range(length_2):
    numbers_set2.add(input())

matching_elements = numbers_set1.intersection(numbers_set2)

result = [int(x) for x in matching_elements]

print(*result, sep="\n")