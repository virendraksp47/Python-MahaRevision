dict1={"a": 1, "b": 2}
dict2={"c": 3, "d": 4}

# Method 1: Using the update() method
merged_dict = dict1.copy()  # Create a copy of dict1 to avoid modifying it
merged_dict.update(dict2)  # Update the copy with dict2
print("Merged Dictionary using update():", merged_dict)

# Method 2: Using the unpacking operator (**)
merged_dict_unpacking = {**dict1, **dict2}  # Unpack both dictionaries into a new one
print("Merged Dictionary using unpacking operator:", merged_dict_unpacking) 

# Method 3: Using the | operator (Python 3.9+)
merged_dict_pipe = dict1 | dict2  # Merge dictionaries using the | operator
print("Merged Dictionary using | operator:", merged_dict_pipe)