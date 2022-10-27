n = int(input())

row = 1
even_set = set()
odd_set = set()

for _ in range(n):
    name = input()
    summary = 0
    for el in name:
        summary += ord(el)
    num = summary // row
    if num % 2 == 0:
        even_set.add(num)
    else:
        odd_set.add(num)

    row += 1

if sum(even_set) == sum(odd_set):
    whole_set = odd_set.union(even_set)
    print(", ".join([str(x) for x in whole_set]))
elif sum(odd_set) > sum(even_set):
    diff = odd_set.difference(even_set)
    print(", ".join([str(x) for x in diff]))
else:
    symmetric_diff = odd_set.symmetric_difference(even_set)
    print(", ".join([str(x) for x in symmetric_diff]))