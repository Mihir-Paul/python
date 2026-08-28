t=(1,2,3)
print(t)
t1=(10)
print(type(t1))
t2=(10,)
print(type(t2))

tup=(1,2,3,4,5)
a1,*b1,c1=tup
print(a1)
print(b1)
print(c1)

tup1=(90,80,70)
tup2=(60,50,40)
tup3=tup1+tup2
print(tup3)

t3=(10,20,20,30,40,50)
a,*b,c,d,= t3
print(a)
print(b)
print(c)
print(d)
print(t3[1])
print(t3[-2])
print(t3[1:3])
print(t3[0:6:2])
print(len(t3))
print(t3.index(20))
print(t3.count(20))
del (t)
t=20,
print(t)