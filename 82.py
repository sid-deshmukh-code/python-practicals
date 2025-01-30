set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection = set1.intersection(set2)
union = set1.union(set2)
difference = set1.difference(set2)
symmetric_difference = set1.symmetric_difference(set2)

print(intersection)
print(union)
print(difference)
print(symmetric_difference)

set1.clear()
print(set1)
