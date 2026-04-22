from functools import reduce

list1=[23,89,75,90,17,64,85,45,67,34]

def greater(x,y):
    if x>y:
        return x
    else:
        return y   
    
largest=reduce(greater,list1)
print(largest)