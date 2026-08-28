a=20
print(type(a))
b=10.98
print(type(b))
c=4+2j
print(type(c))
d=False
print(type(d))
e=None
print(type(e))

str="aizen","lemon" 
lst=[1,2,3]
tuple=(10,20,30)
set={1,2,3}
dic={"apple":10,"banana":20}
print(type(str))
print(type(lst))
print(type(tuple))
print(type(set))
print(type(dic))

a=type("a",(),{"n":5,"show":lambda self :self.n})
obj=a()

print(type(obj))
print(obj.show())