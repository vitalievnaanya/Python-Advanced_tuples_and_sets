text = input()

dict_count = {}

for el in text:
    if el not in dict_count:
        dict_count[el] = 0
    dict_count[el] += 1

sorted_dict = dict(sorted(dict_count.items(), key= lambda x:x[0]))

for key, value in sorted_dict.items():
    print(f'{key}: {value} time/s')