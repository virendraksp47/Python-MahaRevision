set1=set() #Creating an empty set
set1.add(3) #Adding element to set
print(set1)
set1.add("virendra")
print(set1)
set1.update([1,2,3,4]) #Adding multiple elements to set
print(set1)
set1.remove(3) #Removing element from set
print(set1)
set1.discard("virendra") # No Error Removing element from set
print(set1)
print(len(set1)) #Finding length of set
print(set1.pop()) #Removing and returning an arbitrary element from set

