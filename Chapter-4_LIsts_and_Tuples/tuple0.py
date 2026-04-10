tuple_0=("virendra","pradeep",12,True,5.6)
print(type(tuple_0))

# methods of tuple
co=tuple_0.count(5.6)
print(co)
ind=tuple_0.index("pradeep")
print(ind)
# tuples are immutable
# tuple_0[0]="xyz" # this will give error
print(tuple_0)
# slicing of tuple
print(tuple_0[4:])
print(tuple_0[0:3])

# concatenation of tuple
tuple1=(1,2,3)
tuple2=("a","b","c")
tuple3=tuple1+tuple2
print(tuple3)
print(tuple3*2)

# repetition of tuple
tuple4=("virendra",)*5
print(tuple4)
# nested tuple
tuple5=(1,2,(3,4),("a","b"))
print(tuple5)  
print(tuple5[2][0]) # accessing nested tuple element


# unpacking of tuple
tuple6=("virendra","pradeep",12)
name1,name2,age=tuple6
print(name1)   
print(name2)
print(age)
print(tuple6)
