class employee():
    a=1

class programmer(employee):
    b=2

class coder(programmer):
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