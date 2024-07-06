import random

# Function to get user's choice
def UserChoice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

# Function to generate computer's choice
def ComputerChoice():
    ch = ['rock', 'paper', 'scissors']
    return random.choice(ch)

# Function to determine the winner
def DetermineWinner(u_choice, c_choice):
    if u_choice == c_choice:
        return 'tie'
    elif (u_choice == 'rock' and c_choice == 'scissors') or (u_choice == 'scissors' and c_choice == 'paper') or (u_choice == 'paper' and c_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

# Main function to run the game
 
print("===== Rock-Paper-Scissors Game =====")
user_score = 0
computer_score = 0
round_number = 1
    
while True:
    print(f"\n===== Round {round_number} =====")
    user_choice = UserChoice()
    computer_choice = ComputerChoice()
        
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
        
    winner = DetermineWinner(user_choice, computer_choice)
        
    if winner == 'user':
        print("You win this round!")
        user_score += 1
    elif winner == 'computer':
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie this round!")
    print(f"\nScore - You: {user_score}, Computer: {computer_score}")       
    play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\nThanks for playing!")
        break
        
    round_number += 1