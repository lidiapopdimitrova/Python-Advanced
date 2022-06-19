def is_vip(guest):
    return guest[0].isdigit()


n = int(input())
vip_set = set()
regular_set = set()

for _ in range(n):
    current_guest = input()
    if is_vip(current_guest):
        vip_set.add(current_guest)
    else:
        regular_set.add(current_guest)


while True:
    guest = input()
    if guest == "END":
        break

    if is_vip(guest):
        vip_set.remove(guest)

    else:
        regular_set.remove(guest)

print(len(vip_set) + len(regular_set))
[print(guest) for guest in sorted(vip_set)]
[print(guest) for guest in sorted(regular_set)]