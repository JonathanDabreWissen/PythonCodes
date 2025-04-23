#  Positional Parameters

def emp1(name, age, sal, des):
    print("Name: ", name)
    print("Age: ", age)
    print("Salary: ", sal)
    print("Designation: ", des)
    

emp1("Mukhtapuram Nandini", 30,  99000, "Developer")
print("---------------------------------------------")

# Keyworded Parameters

def emp2(name, age, sal, des):
    print("Name: ", name)
    print("Age: ", age)
    print("Salary: ", sal)
    print("Designation: ", des)
    
emp2(age=31, sal=98000, name="Ramajaneyulu", des="Manager")

print("---------------------------------------------")

# Default Parameters

def emp3(name, age, sal=97000, des="Tester"):
    print("Name: ", name)
    print("Age: ", age)
    print("Salary: ", sal)
    print("Designation: ", des)
    
    
emp3("Ramanujan", age=29)
emp3("Shashi Ranjan", 32, 96000)
emp3(age=34, name="Rohit Sharma")

print("---------------------------------------------")


#Variable Arguments
def emp4(*a): 
    for i in a:
        print(i)
        
        
emp4("Pinak Dhar")
emp4("Ayush Mhatre", 17, 300000, "ayushmhatre@gmail.com")
print("---------------------------------------------")

#Keyword Variable Arguments
def emp5(**a): 
    for i in a:
        print(i)
        
emp5(name="Jonathan", age=21, salary=69000, des="Developer")