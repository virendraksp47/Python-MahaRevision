from random import randint

actual_number=randint(1,10)
number_of_guesses=0
print("Welcome to the Perfect Guess Game!")
print("I have selected a number between 1 and 10. Can you guess it?")
while True:
    guess=int(input("Enter your guess: "))
    number_of_guesses+=1
    if guess==actual_number:
        print(f"Congratulations! You've guessed the number in {number_of_guesses} guesses!")
        break
    elif guess<actual_number:
        print("Too low! Try again.")
    else:        print("Too high! Try again.")
