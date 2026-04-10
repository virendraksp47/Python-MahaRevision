# while loop
i=1
while i<6:
    print(i)
    i+=1
'''
Output:
1
2
3
4
5
'''
list1=[1,"virendra",False,"this","shivaji",2.5]

for item in list1:
    print(item)

j=0
while j<len(list1):
    print(list1[j])
    j+=1

for item in range(len(list1)):
    print(list1[item])