try:
    x = int(input("Enter an even number: "))
    assert x%2 == 0, "You have entered an invalid input or odd number"
except AssertionError as y:
    print(y)

print("Success")

    