n = int(input("Enter the integer:"))
if n>0:
    if n%2==0:
        print(f"{n} is positive even number")
    else:
        print(f"{n} is positive odd number")
elif n<0:
    if n%2==0:
        print(f"{n} is negative even number")
    else:
        print(f"{n} is negative odd number")
else:
    print("Number is Zero")