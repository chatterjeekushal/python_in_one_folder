
# wright a python program to find the maximum and minimum k elements in trapul

mytuple=(4,9,1,7,3,6,5,2)

k=2

sorted_coll= sorted(list(mytuple))

vals=tuple(sorted_coll[:k]+sorted_coll[-k:])

print("tuple:",mytuple)
print("k maximum and minimum valus:",vals)

