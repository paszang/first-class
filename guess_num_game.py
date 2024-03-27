# imporying random number 
import random

# generate a random number between 1 to 10 
secret_number = random.randint(1,10)

# maximum attempts allowed
max_attempt = 3

# function to display a welcome message
def welcome_message():
     print("\nwelcome to the Number Guessing Game!")
     print(f"You have{max_attempt} attempts to guess the correct number.")

#function for recursive guessing
def guess_recursive(attempts_left):
     
#get user input
     guess = int(input("\nGuess the number (between 1 and 10):"))

#check if the guess is correct
     if guess == secret_number:
          print("congratulation! You have guessed the correct number!")
     else:
          print(f"Wrong guess. Attempt left: {attempts_left-1}")
          if attempts_left >1:
               #make a recursive call for another guess
               guess_recursive(attempts_left-1)
          else:
               print(f"\nSorry you couldn't guess the number. The correctr number was{secret_number}.")

# calling the function 
welcome_message()
guess_recursive(max_attempt)

#using id() to get memory addresses
print(f"memory address of secret number {secret_number} is: {id(secret_number)}")
