'''
1 for snake
-1 for water
0 for gun
'''
import random
comp=random.choice(['1','-1','0'])
dict={'1':'snake','-1':'water','0':'gun'}
user=input("Enter 1 for snake, -1 for water and 0 for gun: ")
if user==comp:
    print("It's a tie")
elif (user=='1' and comp=='-1') or (user=='-1' and comp=='0') or (user=='0' and comp=='1'):
    print(f"{dict[comp]} is the computer's choice and {dict[user]} is your choice")
    print("You win")
else:   
    print(f"{dict[comp]} is the computer's choice and {dict[user]} is your choice")
    print("You lose")
