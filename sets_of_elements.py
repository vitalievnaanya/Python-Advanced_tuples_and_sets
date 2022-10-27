n = [int(n) for n in input().split()]

numbers = set()
left_nums = set()

for _ in range(sum(n)):
    num = int(input())
    if num not in numbers:
        numbers.add(num)
    else:
        left_nums.add(num)

for num in left_nums:
    print(num)