# Adding integers
a = 5
b = 3
print("int + int =", a + b)

# Adding floating-point numbers
c = 2.5
d = 4.7
print("float + float =", c + d)

# Adding integer and float
print("int + float =", a + c)

# Concatenating strings
e = "Hello"
f = " World"
print("str + str =", e + f)

# Joining lists
g = [1, 2, 3]
h = [4, 5]
print("list + list =", g + h)

# Example that would cause an error (string + integer)
# print(e + 25)  # This would raise a TypeError

# Correct way to combine string and int (convert int to string)
# i think i dont like python lmao
print("str + int (fixed) =", e + str(25))
