from collections import deque
data = input().split()
numbers = deque()

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for ch in data:
    if ch in "-+*/":
        while len(numbers) > 1:
            first = int(numbers.popleft())
            second = int(numbers.popleft())
            function = operations[ch]
            numbers.appendleft(function(first, second))

    else:
        numbers.append(ch)

[print(x) for x in numbers]
