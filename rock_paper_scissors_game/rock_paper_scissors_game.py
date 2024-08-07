import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def decide_winner(user_choice, computer_choice):
    winning_cases = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if user_choice == computer_choice:
        return 'tie'
    elif winning_cases[user_choice] == computer_choice:
        return 'win'
    else:
        return 'lose'

def show_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose!")
    else:
        print("It's a tie!")

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ")
        if user_choice == 'quit':
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        result = decide_winner(user_choice, computer_choice)
        show_result(user_choice, computer_choice, result)

        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nScore: You {user_score} - Computer {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again != 'yes':
            break

    print("\nThanks for playing! Final Score:")
    print(f"You: {user_score} - Computer: {computer_score}")

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()