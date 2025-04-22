lst = [10, 20, 20, "Pritam Singh", 34]

lst.append(40)
print(lst)

lst.remove("Pritam Singh")
print(lst)

del lst[0]
print(lst)

print(max(lst))
print(min(lst))

lst.insert(3, 50)
print(lst)

lst.sort()
print(lst)


lst.sort(reverse=True)
print(lst)
