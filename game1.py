
import random
def game():
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    user = input("Enter rock / paper / scissors: ").lower()

    if user == computer:
        print("Draw!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("Computer Wins!")

    print("Computer chose:", computer)

again = "yes"
while again == "yes" or again == "y":
    game()
    again = input("Play again? (yes/no): ").lower()
    if again != "yes" and again != "y":
        print("Thanks for playing!")
        break