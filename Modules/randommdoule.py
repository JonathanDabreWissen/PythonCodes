from random import *

for i in range(10):
    print(random())
    
    
for i in range(10):
    print(randint(1, 40))
    
for i in range(10):
    print(uniform(1, 40))
    

for i in range(10):
    print(randrange(10))
    print(randrange(1, 15))
    print(randrange(1, 30, 3))
    
    
lst = ["Python", "Flask", "Apache Airflow", "JAVA"]

for i in range(10):
    print(choice(lst))