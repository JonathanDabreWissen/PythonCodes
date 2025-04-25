import logging

logging.basicConfig(filename="sample.log", level=logging.DEBUG)

try:
    f = open("textfile", "w") 
    a,b = [int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c = a/b
    f.write("Writing %d into the file" %c)
    
except ZeroDivisionError:
    print("Division by Zero is not allowed")
    print("Please enter a non-zero number")
    logging.error("Division by zero error")

else:
    print("You have entered a non-zero number")

finally:
    f.close()
    print("File is closed")