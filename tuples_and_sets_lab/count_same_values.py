numbers_string = input()

occurrences_count = {}
# no such thing as tuple comprehension, this is a generator
numbers = [float(x) for x in numbers_string.split()]

for num in numbers:
    if num not in occurrences_count:
        occurrences_count[num] = 0
    occurrences_count[num] += 1

for number, count in occurrences_count.items():
    print(f"{number:.1f} - {count} times")