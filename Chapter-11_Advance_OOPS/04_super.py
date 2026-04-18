class employee():
    def __init__(self):
        print("This is employee class")
    a=1

class programmer(employee):
    def __init__(self):
        super().__init__()
        print("This is programmer class")
    b=2

class coder(programmer):
    def __init__(self):
        super().__init__()
        print("This is coder class")
    c=3

a=employee()
print(a.a)
b=programmer()
print(b.a)
print(b.b)
c=coder()
print(c.a) 
print(c.b)
print(c.c)