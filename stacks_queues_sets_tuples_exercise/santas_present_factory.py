from collections import deque


def is_equal(magic_levels, materials):
    materials.pop()
    magic_levels.popleft()


materials_for_crafting_toys = [int(x) for x in input().split()]
magic_level = deque([int(x)for x in input().split()])

doll = 150
doll_count = 0
wooden_train = 250
wooden_train_count = 0
teddy_bear = 300
teddy_bear_count = 0
bicycle = 400
bicycle_count = 0


while magic_level and materials_for_crafting_toys:
    total_magic_level = materials_for_crafting_toys[-1] * magic_level[0]
    if total_magic_level == doll:
        is_equal(magic_level, materials_for_crafting_toys)
        doll_count += 1
    elif total_magic_level == wooden_train:
        is_equal(magic_level, materials_for_crafting_toys)
        wooden_train_count += 1
    elif total_magic_level == teddy_bear:
        is_equal(magic_level, materials_for_crafting_toys)
        teddy_bear_count += 1
    elif total_magic_level == bicycle:
        is_equal(magic_level, materials_for_crafting_toys)
        bicycle_count += 1

    elif total_magic_level > 0:
        magic_level.popleft()
        materials_for_crafting_toys[-1] += 15

    if total_magic_level < 0:
        result = materials_for_crafting_toys.pop() + magic_level.popleft()
        materials_for_crafting_toys.append(result)

    if total_magic_level == 0:
        if magic_level[0] == 0:
            magic_level.popleft()
        else:
            materials_for_crafting_toys.pop()

if doll_count >= 1 and wooden_train_count >= 1:
    print("The presents are crafted! Merry Christmas!")
elif teddy_bear_count >= 1 and bicycle_count >= 1:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if materials_for_crafting_toys:
    print(f"Materials left: {', '.join(str(x) for x in materials_for_crafting_toys[::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")


if bicycle_count > 0:
    print(f"Bicycle: {bicycle_count}")
if doll_count > 0:
    print(f"Doll: {doll_count}")
if teddy_bear_count > 0:
    print(f"Teddy bear: {teddy_bear_count}")
if wooden_train_count > 0:
    print(f"Wooden train: {wooden_train_count}")