from collections import deque

elf_energy = deque(int(x) for x in input().split())
materials_in_box = [int(x) for x in input().split()]
toys_crafted = 0
energy_used = 0
attempts = 1

while materials_in_box and elf_energy:

    while elf_energy and elf_energy[0] < 5:
        elf_energy.popleft()
    if not elf_energy:
        break

    current_elf = elf_energy[0]
    current_box = materials_in_box[-1]

    if attempts % 3 != 0 and attempts % 5 != 0 and current_box <= current_elf:
        toys_crafted += 1
        energy_used += current_box
        elf_energy[0] -= current_box
        elf_energy[0] += 1
        materials_in_box.pop()
        elf_energy.append(elf_energy.popleft())
    elif attempts % 3 == 0 and attempts % 5 != 0 and (current_box * 2) <= current_elf:
        toys_crafted += 2
        energy_used += current_box * 2
        elf_energy[0] -= current_box * 2
        elf_energy[0] += 1
        materials_in_box.pop()
        elf_energy.append(elf_energy.popleft())
    elif attempts % 3 != 0 and attempts % 5 == 0 and current_box <= current_elf:
        energy_used += current_box
        elf_energy[0] -= current_box
        materials_in_box.pop()
        elf_energy.append(elf_energy.popleft())
    elif attempts % 3 == 0 and attempts % 5 == 0 and (current_box * 2) <= current_elf:
        energy_used += current_box * 2
        materials_in_box.pop()
        elf_energy.append(elf_energy.popleft())
    elif current_box > current_elf or (current_box * 2) > current_elf:
        elf_energy[0] *= 2
        elf_energy.append(elf_energy.popleft())

    attempts += 1


print(f"Toys: {toys_crafted}")
print(f"Energy: {energy_used}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")

if materials_in_box:
    print(f"Boxes left: {', '.join(str(x) for x in materials_in_box)}")

