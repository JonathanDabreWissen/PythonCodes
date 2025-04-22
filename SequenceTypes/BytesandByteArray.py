lst = [10, 20, 30, 40, 50]
print(type(lst))
b = bytes(lst)
print(type(b))
print(b)

# We cannot add (or) update elements to bytes array
# b[3] = 60


b1 = bytearray(lst)
print(type(b1))
