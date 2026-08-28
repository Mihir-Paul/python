try:
    a = int(input("Enter a number:"))
    print(1/a)
except ZeroDivisionError:
    print("Number cannot be divided by zero.")
except ValueError:
    print("Pass a number!")
except AnyOtherException:
    print("Something went wrong")
finally:
    print("Cleanup Required")