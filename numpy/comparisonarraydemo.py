from numpy import *

a1 = array([20, 40, 60, 80, 100])


a2 = array([10, 20, 30, 45, 60])


print(a1>=a2)
print(a1<a2)

print(any(a1>=a2))
print(all(a1 >= a2))

a3 = array([21, 10, 9, 8])
a4 = array([10, 20, 30, 40])

print(where(a3%2 != 0, a3, 250))

print(where(a3>a4, a3, a4))