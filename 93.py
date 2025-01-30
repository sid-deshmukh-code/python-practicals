d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = {}
for key in d1:
    combined_dict[key] = d1[key] + d2.get(key, 0)
for key in d2:
    if key not in combined_dict:
        combined_dict[key] = d2[key]
print(combined_dict)
