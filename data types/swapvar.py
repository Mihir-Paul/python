#Using temp variable
x=30
y=70
temp=x
x=y
y= temp
print(x)
print(y)

#Using tuple functions
x=30
y=70
y,x=x,y
print(x)
print(y)

#Using Arithmetic operator
x=30
y=70
x=x+y
y=x-y
x=x-y

print(x)
print(y)
