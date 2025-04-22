s = "You are awesome"
print(s)

s1 = """You are the creator of your own destiny"""

print(s1)
print(s[2])

print(s*3)
print(len(s))
print(len(s1))

s = "0123456789"
# Slicing
print("Slicing")
print(s)
print(s[0:5])
print(s[0:])
print(s[2:])
print(s[:9])
print("what")
print(s[-4:1])
print("what")

# Step in slicing
print(s[0:8:2])
print(s[15::-1])

# Strip ---> Removing the whitespaces
s2 = "   Welcome Folks   "
print(s2.rstrip())
print(s2.lstrip())
print(s2.strip())


print(s2.count("o"))
print(s2.replace("Folks", "Guys"))
print(s2.upper())
print(s2.lower())
