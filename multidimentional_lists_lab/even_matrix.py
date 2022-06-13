def is_even(num):
    return num % 2 == 0


number = int(input())

result = []

for _ in range(number):
    row = [int(x) for x in input().split(', ')]
    result.append(
        [int(x) for x in row if is_even(x)]
    )

print(result)