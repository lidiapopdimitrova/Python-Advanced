number = int(input())
row = 1
odd_numbers_set = set()
even_numbers_set = set()

for n in range(number):
    result = 0
    name = input()

    for letter in name:
        result += ord(letter)

    final_sum = int(result / row)
    if final_sum % 2 == 0:
        even_numbers_set.add(final_sum)
    else:
        odd_numbers_set.add(final_sum)

    row += 1

sum_even = sum(even_numbers_set)
sum_odd = sum(odd_numbers_set)

if sum_even > sum_odd:
    intersection = odd_numbers_set & even_numbers_set
    union = even_numbers_set | odd_numbers_set
    for i in intersection:
        union.remove(i)
    print(", ".join(map(str, union)))

elif sum_even < sum_odd:
    difference = odd_numbers_set - even_numbers_set
    print(", ".join(map(str, difference)))
else:
    union = even_numbers_set | odd_numbers_set
    print(", ".join(map(str, union)))