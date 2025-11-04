a = {1,2,3,4}
b = {4,5,6,7,8}

for i in a:
    print(i)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.update(b))
print(a.add(9))
print(a.remove(9))

