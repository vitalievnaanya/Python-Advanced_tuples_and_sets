n = int(input())

parking_lot = set()

for _ in range(n):
    command, car_num = input().split(', ')
    if command == 'IN':
        parking_lot.add(car_num)
    else:
        parking_lot.remove(car_num)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print(f'Parking Lot is Empty')