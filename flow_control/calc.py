print("""Enter Choice:
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division"""
    
)

choice = int(input("Enter the choice between 1 and 4:"))
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
if choice ==1:
    result = a+b
elif choice ==2:
    result = a-b
elif choice ==3:
    result = a*b
elif choice ==4:
    result = a/b
else:
    print("Invalid input")
    
print("The result:",result)