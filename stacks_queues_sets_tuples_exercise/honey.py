from collections import deque

bee_values = deque([int(x)for x in input().split()])
nectar_values = [int(x) for x in input().split()]
operations = deque(input().split())

honey = 0

operations_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

while bee_values and nectar_values:
    first_bee = bee_values.popleft()
    last_nectar = nectar_values.pop()
    if last_nectar < first_bee:
        bee_values.appendleft(first_bee)
        continue
    if last_nectar == 0:
        continue

    operator = operations.popleft()
    honey += abs(operations_dict[operator](first_bee, last_nectar))


print(f"Total honey made: {honey}")
if bee_values:
    print(f"Bees left: {', '.join(str(x) for x in bee_values)}")
if nectar_values:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_values)}")