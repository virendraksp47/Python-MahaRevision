marks={"virendra": 98,
     "ajay": 87,
     "sachin": 78,
     "list":[1,2,3,4]}
# dictionary methods
#print(marks.values())
marks.update({"virendra":90,"jaya":85}) # updating value of existing key and adding new key-value pair
#print(marks.keys())
print(marks.get("vire"))  # accessing value using get() method and does not throw error if key is not found
print(marks["virendra"]) # accessing value using key directly and throws error if key is not found
print(marks.pop("ajay")) # removes key-value pair and returns value of removed key
print(marks.popitem()) # removes last inserted key-value pair and returns it as tuple
