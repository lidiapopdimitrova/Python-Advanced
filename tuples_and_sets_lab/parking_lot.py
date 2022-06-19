num = int(input())

commands = [input().split(", ") for _ in range(num)]

parking_lot = set()

for direction, car_number in commands:
    if direction == "IN":
        parking_lot.add(car_number)
    else:
        parking_lot.remove(car_number)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print("Parking Lot is Empty")
