# map example
l = [1, 2, 3, 4, 5]
square=lambda x: x*x
squared_list = list(map(square, l))
print(squared_list)  

# filter example
def even(n):
    return n % 2 == 0
even_list = filter(even, l)
print(list(even_list))  # Output: [2, 4]

# reduce example
from functools import reduce
def add(x, y):
    return x + y
sum_of_list = reduce(add, l)
print(sum_of_list)  # Output: 15