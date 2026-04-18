n=int(input("Enter a number "))
m=int(input("Enter second number "))

if m==0:
    raise ZeroDivisionError("Hey our program is not meant to" \
    "divide numbers by zero")
else :
    print(f"The divison n/m is {n/m}")