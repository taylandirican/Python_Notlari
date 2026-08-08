#value types => str, number
x = 4
y = 12

x = y
print(x,y)

y = 10

print(x,y)

#reference types => list
a = ["cherry", "banana"]
b = ["apple", "banana"]
print(a,b)
a = b
print(a,b)
b[0] = "grape"
print(a,b)

