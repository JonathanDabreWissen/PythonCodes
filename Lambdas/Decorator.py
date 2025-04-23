# Decorator ---> It takes a function and returns a function and perform additional logic to it

def decorfun(fun):
    def inner():
        result = fun()
        return result * 2
    
    return inner

@decorfun
def num():
    return 1000


print(num())