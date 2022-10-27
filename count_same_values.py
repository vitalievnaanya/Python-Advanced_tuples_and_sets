numbers = input().split()

nums_count = {}

for num in numbers:
    if num not  in nums_count:
        nums_count[num] = 0
    nums_count[num] += 1

for key, value in nums_count.items():
    print(f'{float(key):.1f} - {value} times')