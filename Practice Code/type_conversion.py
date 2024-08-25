# Python takes care of the type identifying process
a = 70  # integer
b = 12.5  # float
c = "Hello World"  # string
d = True  # boolean
e = None  # NoneType
comp = 2 + 7j  # complex

print("a = ", a, "\nType of a is ", type(a))
print("b = ", b, "\nType of b is ", type(b))
print("c = ", c, "\nType of c is ", type(c))
print("d = ", d, "\nType of d is ", type(d))
print("e = ", e, "\nType of e is ", type(e))
print(f"is {comp} a complex number? ", isinstance(comp, complex))

# converting between types
# Converting string to number
x = "56"
print(int(x))  # int

# Converting int to float
p = 12
print(float(p))  # float

# Converting float to int
q = 452.98
print(int(q))  # int

# Converting int to string
print(str(p))  # str
