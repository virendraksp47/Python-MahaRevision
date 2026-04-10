# lists methods
list1=[1,2,3,10,9,5,6,7,8]
print(list1)

list1.append(47) # this will append item in last
list1.sort() # sort numerical lists
list1.reverse()
print(list1)
list1.insert(len(list1), "xyz")
print(list1)
value=list1.pop(-1) # removes last item
print(value)
print(list1)