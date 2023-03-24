import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ["rock", "paper", "scissors"]
    
    score = {
        "user": 0,
        "computer": 0
    }
    
    while True:
        computer_choice = random.choice(choices)
        user_choice = input("Choose 'rock', 'paper', 'scissors' or type 'quit' to exit: ").lower()
        
        if user_choice == "quit":
            break
        
        if user_choice not in choices:
            print("Invalid input. Please choose 'rock', 'paper', 'scissors' or type 'quit' to exit.")
            continue

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            score["user"] += 1
        else:
            print("Computer wins!")
            score["computer"] += 1

        print(f"Score: You {score['user']} - {score['computer']} Computer")
        
if __name__ == "__main__":
	main()
