#  Generator ---> sequence of values/ range datatype / yield (storing each value in sequence)


# Generator --> Handle the Asynchronous data streams 

# Yield ---> Create memory efficient iterators


def customgen(a, b):
    while a<b:
        yield a
        a +=4
        
result = customgen(10, 50)

for i in result: print(i)