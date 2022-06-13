# import random module 
import random 
  
# Print multiline instruction 
# performstring concatenation of string 
print ("Winning rules of the rock paper scissors game is as follows: \n"
+ "Rock vs paper ->paper wins \n"
+ " Rock vs scissors -> Rock wins \n"
+ "paper vs scissors -> scissors wins \n")
 # possible_choices = ["R" = "rock", "P" = "paper", "S" = "scissor"] 
while True:
    choice = (input("User turn: "))
    possible_choices = ["R", "P", "S"]
    computer_choice = random.choice(possible_choices)
    print(f"\nYou chose {choice}, computer chose {computer_choice}.\n") 
    if choice == computer_choice:
        print(f"Both players selected {choice}. It's a tie!")
    elif choice == "R":
        if computer_choice== "S":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif choice == "P":
        if computer_choice == "R":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break