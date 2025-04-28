from numpy import *

a1 = arange(1, 10)
a2 = a1.copy()
a3 = a1.view()

print(a1)
print(a2)
print(a3)