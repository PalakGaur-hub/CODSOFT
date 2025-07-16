#rock-paper-scissor game
import random

# Possible choices
choices = ['rock', 'paper', 'scissors']

# Score tracking
user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_round():
    global user_score, computer_score

    # User Input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    # Computer Selection
    computer_choice = random.choice(choices)

    # Game Logic
    winner = get_winner(user_choice, computer_choice)

    # Display Result
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if winner == 'tie':
        print("Result: It's a tie!")
    elif winner == 'user':
        print("Result: You win!")
        user_score += 1
    else:
        print("Result: You lose!")
        computer_score += 1

    # Show Scores
    print(f"\nScore => You: {user_score} | Computer: {computer_score}\n")

def main():
    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        play_round()

        # Play Again
        again = input("Do you want to play another round? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break

# Start the game
main()
