from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

gemstone_count = 0
gemstone_dict = []
porcelain_dict = []
gold_dict = []
diamond_dict = []
porcelain_count = 0
gold_count = 0
diamond_count = 0

is_succeeded = False

while materials and magic_levels:
    last_material = materials[-1]
    first_magic = magic_levels[0]
    result = last_material + first_magic
    if 100 <= result <= 199:
        gemstone_count += 1
        gemstone_dict.append(result)
        materials.pop()
        magic_levels.popleft()
    elif 200 <= result <= 299:
        porcelain_count += 1
        porcelain_dict.append(result)
        materials.pop()
        magic_levels.popleft()
    elif 300 <= result <= 399:
        gold_count += 1
        gold_dict.append(result)
        materials.pop()
        magic_levels.popleft()
    elif 400 <= result <= 499:
        diamond_count += 1
        diamond_dict.append(result)
        materials.pop()
        magic_levels.popleft()
    elif result < 100:
        if result % 2 == 0:
            result = last_material * 2 + first_magic * 3
            if 100 <= result <= 199:
                gemstone_count += 1
                gemstone_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            elif 200 <= result <= 299:
                porcelain_count += 1
                porcelain_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            elif 300 <= result <= 399:
                gold_count += 1
                gold_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            elif 400 <= result <= 499:
                diamond_count += 1
                diamond_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            else:
                materials.pop()
                magic_levels.popleft()
        else:
            result = result * 2
            if 100 <= result <= 199:
                gemstone_count += 1
                gemstone_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            elif 200 <= result <= 299:
                porcelain_count += 1
                porcelain_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            elif 300 <= result <= 399:
                gold_count += 1
                gold_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            elif 400 <= result <= 499:
                diamond_count += 1
                diamond_dict.append(result)
                materials.pop()
                magic_levels.popleft()
            else:
                materials.pop()
                magic_levels.popleft()
    elif result > 499:
        result = result / 2
        if 100 <= result <= 199:
            gemstone_count += 1
            gemstone_dict.append(result)
            materials.pop()
            magic_levels.popleft()
        elif 200 <= result <= 299:
            porcelain_count += 1
            porcelain_dict.append(result)
            materials.pop()
            magic_levels.popleft()
        elif 300 <= result <= 399:
            gold_count += 1
            gold_dict.append(result)
            materials.pop()
            magic_levels.popleft()
        elif 400 <= result <= 499:
            diamond_count += 1
            diamond_dict.append(result)
            materials.pop()
            magic_levels.popleft()
        else:
            materials.pop()
            magic_levels.popleft()

if gemstone_count >= 1 and porcelain_count >= 1:
    is_succeeded = True

if gold_count >= 1 and diamond_count >= 1:
    is_succeeded = True

if is_succeeded:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")


if diamond_dict:
    print(f"Diamond Jewellery: {diamond_count}")
if gemstone_dict:
    print(f"Gemstone: {gemstone_count}")
if gold_dict:
    print(f"Gold: {gold_count}")
if porcelain_dict:
    print(f"Porcelain Sculpture: {porcelain_count}")


