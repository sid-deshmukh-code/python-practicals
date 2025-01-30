my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
sorted_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print(sorted_asc)
print(sorted_desc)
