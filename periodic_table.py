n = int(input())

elements = set()

for _ in range(n):
    layer = input().split()
    for el in layer:
        elements.add(el)

for element in elements:
    print(element)