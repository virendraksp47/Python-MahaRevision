myList=[1,2,3,4,5]

'''squaredList=[]
for item in myList:
    squaredList.append(item**2)

print(squaredList)'''

squaredList=[item**2 for item in myList]
print(squaredList)