""" 
class LimitException(Exception):
    def __init__(self, msg):
        self.msg=msg
        
    def withdrawal(amount):
        if(amount>60000):
            raise LimitException("You cannot withdraw more than 60000 per day")
        
    
    withdrawal(62000)
    print("You can withdraw the amount")
"""

class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg
        
class TooOldException(Exception):
    def __init__(self, msg):
        self.msg = msg
        
        
age = int(input("Enter the age: "))

if age<18:
    raise TooYoungException("You are not eligible to vote")
elif age> 90:
    raise TooOldException("You have to be younger than age 90 years")
else:
    print("You are eligible to vote")
        
