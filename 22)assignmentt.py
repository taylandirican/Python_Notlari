x, y, z = 5,10,15
print(x, y,z)

x, y = y, x
print(x, y,z)

x = x + 5
print(x, y,z)

# x += 5 # x = x+5
# print(x, y,z)

values = 1, 2, 3 
print(values)
print(type(values))

x, y,z = values
print(x,y,z)

values = 1,2,3,4,5
x, y,*z = values    # * işareti kalan değerleri liste şeklinde atar
print(x,y,z)


print(x,y,z[1])