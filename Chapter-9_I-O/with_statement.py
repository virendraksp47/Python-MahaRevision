f=open("harry.txt")
print(f.read())
f.close()

#with statement
with open("harry.txt") as f:
    print(f.read())