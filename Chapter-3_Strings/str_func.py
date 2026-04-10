name="virendra kashyap" # this is a string
#length of string
#print(len(name))

# methods in string
print(name.endswith("x")) #check if string ends with given character
print(name.startswith("v")) # check if string starts with given character
print(name.capitalize()) # capitalize first letter
print(name.upper())# convert to uppercase
#print(name.lower())
print(name.find("kash"))# find index of substring
print(name.replace("virendra","kumar")) # replace substring with another substring
print(name.count("a")) # count occurrences of substring
#print(name.casefold()) # convert string to casefolded version
print(name.strip()) # remove leading and trailing whitespace
print(name.rstrip()) # remove trailing whitespace
print(name.lstrip()) # remove leading whitespace  
text = name.replace(" ", ",") # replace underscores with commas
print(text)
words=text.split(",") # split string into list using comma as delimiter
print(words)
print(type(words))
sep_list=" ".join(words) # join list elements into string with hyphen as separator
print(sep_list)

name3="virendra \"kashyap\" "
print(name3)