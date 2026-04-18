a= 9

def num():
    global a
    print(f"The value of a is {a}")
    a = 8
    print(f"The value of a is {a}")
num()
print(f"The value of a is {a}")