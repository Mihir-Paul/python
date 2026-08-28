print(id(5))
a=10
print(id(a))
b=a
print(id(b))

a=5
b=5
print(a is b)
c=b 
print(c is a)
c=20
print(c is b)
print(id(a)==id(b))