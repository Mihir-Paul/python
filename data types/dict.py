d={"idfc":17,"sbi":19,"axis":21}
print(d)
d={}
d["python"]=1
d["java"]=2
d["c"]=3
print(d)
print(d["c"])

print(d.get("java"))
print(d.get("c++"))
if "java" in d:
    print(d["java"])
else:
    print("Nah")
    
d["c++"]=4
d["php"]=5
print(len(d))
print(d)

for key in d:
    print(key)
    
for key,value in d.items():
    print(key,value)
    
for values in d.values():
    print(value)
    
print(d.pop("java"))
print(d.popitem())
del d["c"]
print(d)

d= { 
    "Student":{
        "student":"Mihir",
        "age":19,
        "roll":7072
    }}
print(d["Student"]["roll"])