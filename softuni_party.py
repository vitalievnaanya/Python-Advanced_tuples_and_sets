n = int(input())

guests = set()

for _ in range(n):
    guest = input()
    guests.add(guest)

command = input()

while command != 'END':
    guests.remove(command)
    command = input()

print(f'{len(guests)}')

vip_guests = set()
not_vip = set()

for guest in guests:
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        not_vip.add(guest)

for vip in vip_guests:
    print(vip)

for guest in not_vip:
    print(guest)
