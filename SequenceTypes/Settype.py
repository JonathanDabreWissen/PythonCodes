s = {10, 20, 30, "Jonathan Dabre", 10, 20, 40}
print(s)


#  We cannot perform slicing, indexing and repeatition

# print(s*3)
print(type(s))

s.remove(40)
print(s)


#  Frozen Set
f = frozenset(s)
# f.update(100)
# f.remove(10)
print(f)
# Frozenset doesn't perform update and remove operations
