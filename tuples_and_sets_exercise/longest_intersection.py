number = int(input())
longest_intersection = []


for i in range(number):
    set1 = set()
    set2 = set()
    first_intersection, second_intersection = input().split('-')
    i1 = first_intersection.split(",")
    start1 = int(i1[0])
    end1 = int(i1[1])
    i2 = second_intersection.split(",")
    start2 = int(i2[0])
    end2 = int(i2[1])

    for nums in range(start1, end1 + 1):
        set1.add(nums)
    for nums in range(start2, end2 + 1):
        set2.add(nums)

    intersection = set1.intersection(set2)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection


longest = []
for i in longest_intersection:
    longest.append(i)


print(f"Longest intersection is {longest} with length {len(longest)}")
