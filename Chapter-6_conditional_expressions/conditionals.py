age=int(input("Enter your age: "))
# if elif else ladder
if age>=18:
    print("You are above the age of 18, you can vote")
elif age<0:
    print("You entered invalid age")
elif age==0:
    print("You are just born")
else:
    print("You are below the age of 18, you cannot vote")
