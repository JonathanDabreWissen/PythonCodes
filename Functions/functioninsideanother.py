# Function inside another function
def display(name):
    
    def message():
        return "Python"
    
    result = message() + name
    
    return result

print(display(" is a very good programming language"))


# Function parameter

def name():
    return "Welcome folks"

print(display(name()))