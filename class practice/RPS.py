# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice is "r" and computer_choice is "s") or (user_choice is "p" and computer_choice is "r") or (user_choice is "s" and computer_choice is"p")
    print ("You win!")
elif (user_choice is"r" and computer_choice is "p") or (user_choice is "p" and computer_choice is "s") or (user_choice is "s" and computer_choice is "r")
    print ("You lose!")
else:
    print ("Tie")