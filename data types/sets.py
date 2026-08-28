s1={1,2,3}
print(s1)
s2={2,3,4}
print(s2)
s3={}
print(type(s3))
s4=set()
print(type(s4))

s={10,20,30,40,50}
print(s)
s.discard(40)
print(s)
s.remove(20)
print(s)
s.clear()
print(s)
s.add(90)
s.update([70,80])
print(s)
del s

a1={2,4,6,8,9}
a2={3,6,9}
print(a1.union(a2))
print( a1.intersection(a2))
print(a1.difference(a2))
print(a1.symmetric_difference(a2))

a3={6,12,18,24,30}
a4={12,24}

print(a3.isdisjoint(a4))

#Subset
print(a3<=a4)

#Proper Subset
print(a3<a4)

#Superset
print(a3>=a4)

#Proper superset
print(a3>a4)