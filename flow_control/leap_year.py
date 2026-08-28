year = int(input("Enter a number:"))
if year%4 ==0 and year%100 !=0:
    print(f"{year} is a leap year")
elif year%400 == 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")